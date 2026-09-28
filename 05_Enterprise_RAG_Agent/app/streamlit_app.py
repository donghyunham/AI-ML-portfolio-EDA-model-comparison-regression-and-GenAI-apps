import os
import streamlit as st
from agent import MeetingSummaryAgent

st.set_page_config(page_title="Enterprise RAG Meeting Summarizer", page_icon="📝", layout="wide")

st.title("Enterprise RAG: Meeting Summarizer")
st.caption("AWS Bedrock & Retrieval-Augmented Generation (RAG) 기반 회의록 요약 및 Action Item 추출 시스템")

st.sidebar.header("Settings")
region = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
model_id = os.getenv("BEDROCK_MODEL_ID", "global.anthropic.claude-haiku-4-5-20251001-v1:0")
st.sidebar.write(f"AWS Region: {region}")
st.sidebar.write(f"Bedrock Model: {model_id}")

sample_transcript = """[회의록 - 2026년 8월 AI 프로젝트 리뷰]
참석자: 함동현, 팀원 A

함동현: 이번 주에 Scikit-Learn 파이프라인으로 Data Leakage 문제를 전부 보완했습니다. 
이제 AWS Bedrock 기반의 Meeting Assistant Agent 개발로 넘어갈 차례입니다.

팀원 A: 좋습니다. 파이프라인 모듈화 코드는 제가 8월 12일까지 리뷰를 마칠게요. 
동현님은 Bedrock Agent 구현 및 프롬프트 템플릿 완성을 8월 15일까지 진행해 주시면 될 것 같습니다.

함동현: 네, Claude Haiku 4.5 모델을 기반으로 Task Decomposition과 출력 가드레일을 적용해 구축하겠습니다."""

st.subheader("Meeting Transcript Input")
transcript_input = st.text_area("회의록 텍스트를 입력하거나 기본 샘플을 사용하세요.", value=sample_transcript, height=200, max_chars=5000)

if st.button("RAG 기반 회의록 분석 실행", type="primary"):
    with st.spinner("RAG 검색 및 AWS Bedrock 분석 진행 중..."):
        agent = MeetingSummaryAgent(region_name=region, model_id=model_id)
        result, chunks, used_mock, error_message = agent.process_transcript(transcript_input)

        if used_mock:
            st.error(f"⚠️ 실제 Bedrock 호출에 실패하여 예시(mock) 응답이 표시되고 있습니다.\n\n에러 내용: {error_message}")
        else:
            st.success("✅ 실제 AWS Bedrock 응답입니다. RAG 파이프라인 분석 완료!")

        with st.expander("Context Chunks (LLM에 전달된 문맥)"):
            for idx, chunk in enumerate(chunks, 1):
                st.write(f"**Chunk {idx}:** {chunk}")

        st.markdown("---")
        st.markdown(result)