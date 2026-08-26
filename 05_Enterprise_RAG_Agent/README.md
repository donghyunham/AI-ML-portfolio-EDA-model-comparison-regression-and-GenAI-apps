# 05_Enterprise_RAG_Agent

## 프로젝트 개요
본 프로젝트는 AWS 기반 생성형 AI 에이전트 서비스로, 비구조화된 기업 회의록 및 텍스트 데이터를 분석하여 핵심 안건, 담당자, 이행 기한이 포함된 구조화된 Action Item으로 자동 변환하는 시스템입니다.

---

## Tech Stack
- LLM & Cloud Services: AWS Bedrock
- Language & Framework: Python 3.10+, LangChain
- Prompt Engineering: Task Decomposition, Persona Setting, Output Format Safeguard

---

## Architecture & Workflow

1. Task Decomposition (추론 단계 분할)
   - 단일 프롬프트 방식의 한계를 극복하기 위해 [회의록 분석] -> [안건 분류] -> [Action Item 추출]로 추론 단계를 분할하여 처리 정밀도 향상

2. Persona & Safeguard 적용
   - 페르소나 정의 및 엄격한 Output Format 제약 조건을 설정하여 환각(Hallucination) 현상 방지

3. Action Item Generation
   - 최종 추출된 결과를 담당자별, 우선순위별 구조화된 문서(Markdown/JSON) 형태로 자동 출력

---

## 리트리벌 방식 비교: TF-IDF vs Titan Embeddings

프로젝트 초기에는 TF-IDF 기반의 얕은 리트리벌을 사용했으나, 이후 AWS Bedrock Titan Text Embeddings V2(1024차원 벡터)를 도입해 두 방식을 comparison_results.json 기준으로 정량 비교했다.

### 비교 결과
- 히트율: TF-IDF 83.3퍼센트(6건 중 5건), Titan Embedding 83.3퍼센트(6건 중 5건)로 동일
- 속도: TF-IDF 평균 0.001초대, Titan Embedding 평균 2-7초대로 TF-IDF가 훨씬 빠름
- 두 방식 모두 동일한 케이스(신규 인턴 온보딩 자료 관련 질의)에서 실패

### 실패 원인 분석
실패는 리트리벌 알고리즘 자체의 문제가 아니라, 회의록을 줄 단위로 청킹하는 방식에서 비롯된 구조적 한계로 확인됐다. 질문 문장과 답 문장이 서로 다른 청크로 분리되면서, 질문끼리의 유사도가 질문과 답 사이의 유사도보다 높게 나오는 현상이 원인이었다.

### 기본값 결정
정확도가 동일한 조건에서는 더 빠른 방식을 채택하는 것이 합리적인 엔지니어링 판단이라 보고, process_transcript의 기본 리트리벌 방식은 TF-IDF로 유지했다. Titan Embeddings 기반 함수(retrieve_relevant_chunks_embedding)는 코드베이스에 남겨두어, 향후 청킹 전략 개선 시 재검증할 수 있도록 했다.

---

## 주요 성과 및 인사이트
- 정형화되지 않은 텍스트 데이터를 즉시 실행 가능한 결론으로 자동 변환하여 문서 작성 및 요약 시간 단축
- 시스템 프롬프트 가드레일 설정을 통해 환각률 최소화 및 출력 일관성 확보
- 에이전틱 워크플로우(Agentic Workflow) 설계를 통한 복잡한 추론 문제 해결 역량 검증
- TF-IDF와 Titan Embeddings 두 리트리벌 방식을 정량 비교 검증하고, 실패 원인을 청킹 구조 문제로 규명하여 근거 기반 기술 선택 역량 검증 