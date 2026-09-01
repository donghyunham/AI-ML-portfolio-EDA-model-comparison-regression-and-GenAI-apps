import json
import os
import logging
import time
import boto3
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MeetingSummaryAgent:
    """
    AWS Bedrock 기반 RAG (Retrieval-Augmented Generation) 회의록 에이전트.
    1. Retrieval: 입력 문서를 청크 단위로 분할 및 코사인 유사도 기반 관련 맥락 검색
    2. Generation: 검색된 맥락을 기반으로 Task Decomposition 및 Zero-Hallucination 요약 생성
    """

    def __init__(self, region_name=None, model_id=None):
        self.model_id = model_id or os.getenv("BEDROCK_MODEL_ID", "global.anthropic.claude-haiku-4-5-20251001-v1:0")
        resolved_region = region_name or os.getenv("AWS_DEFAULT_REGION", "us-east-1")
        try:
            self.bedrock = boto3.client(service_name="bedrock-runtime", region_name=resolved_region)
        except Exception as e:
            logger.exception("Bedrock 클라이언트 생성 실패: %s", e)
            self.bedrock = None

        self.last_metrics = {}

    def retrieve_relevant_chunks_tfidf(self, transcript: str, query: str = "액션 아이템 및 주요 결정사항", top_k: int = 3) -> list:
        chunks = [c.strip() for c in transcript.strip().split("\n") if c.strip()]
        if not chunks:
            return []

        vectorizer = TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 4))
        tfidf_matrix = vectorizer.fit_transform(chunks + [query])

        chunk_vectors = tfidf_matrix[:-1]
        query_vector = tfidf_matrix[-1:]

        similarities = cosine_similarity(query_vector, chunk_vectors).flatten()
        top_indices = similarities.argsort()[::-1][:top_k]

        return [chunks[i] for i in top_indices if similarities[i] > 0]

    def _get_embedding(self, text: str) -> list:
        response = self.bedrock.invoke_model(
            modelId="amazon.titan-embed-text-v2:0",
            body=json.dumps({"inputText": text})
        )
        result = json.loads(response['body'].read())
        return result['embedding']

    def retrieve_relevant_chunks_embedding(self, transcript: str, query: str = "액션 아이템 및 주요 결정사항", top_k: int = 3) -> list:
        chunks = [c.strip() for c in transcript.strip().split("\n") if c.strip()]
        if not chunks:
            return []

        chunk_embeddings = [self._get_embedding(c) for c in chunks]
        query_embedding = self._get_embedding(query)

        chunk_matrix = np.array(chunk_embeddings)
        query_vector = np.array(query_embedding).reshape(1, -1)

        similarities = cosine_similarity(query_vector, chunk_matrix).flatten()
        top_indices = similarities.argsort()[::-1][:top_k]

        return [chunks[i] for i in top_indices if similarities[i] > 0]

    def _invoke_bedrock(self, prompt: str) -> str:
        payload = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "messages": [{"role": "user", "content": prompt}]
        }
        response = self.bedrock.invoke_model(
            modelId=self.model_id,
            body=json.dumps(payload)
        )
        result = json.loads(response['body'].read())
        return result['content'][0]['text']

    def _analyze_transcript(self, context_chunks: list) -> str:
        context_text = "\n".join([f"- {chunk}" for chunk in context_chunks])
        prompt = f"""You are an executive AI Meeting Assistant.
Read the meeting transcript excerpts below and identify the key discussion points, decisions, and any mentioned deadlines or responsible people.
Do NOT format the final output yet. Just list the core points you found, in Korean.

[Meeting Transcript]
{context_text}
"""
        return self._invoke_bedrock(prompt)

    def _classify_topics(self, analysis: str) -> str:
        prompt = f"""Based on the meeting analysis below, group the discussion points into distinct topics or agenda items.
For each topic, briefly state what was discussed and who is responsible, if mentioned. Output in Korean as a list of topics.

[Meeting Analysis]
{analysis}
"""
        return self._invoke_bedrock(prompt)

    def _extract_action_items(self, classified_topics: str, query: str) -> str:
        prompt = f"""You are an executive AI Meeting Assistant. Based on the classified topics below, complete the user query.

[Constraints and Safeguards]
Rely ONLY on the classified topics above. Do NOT assume or invent outside facts.
Output strictly in Markdown.

[Classified Topics]
{classified_topics}

[User Query]
{query}

[Output Format]
### 1. Executive Summary
- ...

### 2. Action Items
| Assignee | Action Item | Due Date |
| :--- | :--- | :--- |

### 3. Key Decisions
- ...
"""
        return self._invoke_bedrock(prompt)

    def process_transcript(self, transcript: str, query: str = "회의 요약 및 액션 아이템 추출") -> tuple:
        start_total = time.time()

        start_retrieval = time.time()
        retrieved_chunks = self.retrieve_relevant_chunks_tfidf(transcript, query=query)
        retrieval_time = time.time() - start_retrieval

        context_chunks = retrieved_chunks if retrieved_chunks else [transcript]

        if self.bedrock:
            try:
                start_llm = time.time()

                analysis = self._analyze_transcript(context_chunks)
                classified = self._classify_topics(analysis)
                final_result = self._extract_action_items(classified, query)

                llm_time = time.time() - start_llm

                self.last_metrics = {
                    "retrieval_time_sec": round(retrieval_time, 3),
                    "llm_response_time_sec": round(llm_time, 3),
                    "total_time_sec": round(time.time() - start_total, 3),
                    "retrieved_chunk_count": len(retrieved_chunks),
                    "used_mock": False,
                }
                return final_result, retrieved_chunks, False, None
            except Exception as e:
                logger.exception("Bedrock invoke_model 호출 실패: %s", e)
                self.last_metrics = {
                    "retrieval_time_sec": round(retrieval_time, 3),
                    "llm_response_time_sec": None,
                    "total_time_sec": round(time.time() - start_total, 3),
                    "retrieved_chunk_count": len(retrieved_chunks),
                    "used_mock": True,
                }
                return self._mock_response(), retrieved_chunks, True, str(e)
        else:
            logger.warning("Bedrock 클라이언트가 초기화되지 않아 mock 응답을 반환합니다.")
            self.last_metrics = {
                "retrieval_time_sec": round(retrieval_time, 3),
                "llm_response_time_sec": None,
                "total_time_sec": round(time.time() - start_total, 3),
                "retrieved_chunk_count": len(retrieved_chunks),
                "used_mock": True,
            }
            return self._mock_response(), retrieved_chunks, True, "Bedrock 클라이언트 초기화 실패"

    def _mock_response(self) -> str:
        return """### 1. Executive Summary
- Data Leakage 차단을 위한 Scikit-learn Pipeline 모듈화 검증 완료
- AWS Bedrock 기반 RAG 에이전트 구축 및 테스트 진행

### 2. Action Items
| Assignee | Action Item | Due Date |
| :--- | :--- | :--- |
| 팀원 A | Scikit-learn Pipeline 코드 리뷰 및 Data Leakage 검증 | 2026-08-12 |
| 함동현 | Bedrock Agent 및 Vector Retrieval 파이프라인 구축 | 2026-08-15 |

### 3. Key Decisions
- TF-IDF 및 Cosine Similarity 기반 Retrieval 파이프라인 오케스트레이션 적용
- 환각 현상(Hallucination) 방지를 위한 Context Safeguard 인프라 확정
"""