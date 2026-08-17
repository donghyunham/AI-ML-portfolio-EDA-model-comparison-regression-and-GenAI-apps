# 05_Enterprise_RAG_Agent

## 프로젝트 개요
본 프로젝트는 **AWS 기반 생성형 AI 에이전트 서비스**로, 비구조화된 기업 회의록 및 텍스트 데이터를 분석하여 핵심 안건, 담당자, 이행 기한이 포함된 구조화된 Action Item으로 자동 변환하는 시스템입니다.

---

## Tech Stack
* **LLM & Cloud Services:** AWS Bedrock
* **Language & Framework:** Python 3.10+, LangChain
* **Prompt Engineering:** Task Decomposition, Persona Setting, Output Format Safeguard

---

## Architecture & Workflow

1. **Task Decomposition (추론 단계 분할)**
   - 단일 프롬프트 방식의 한계를 극복하기 위해 [회의록 분석] → [안건 분류] → [Action Item 추출]로 추론 단계를 분할하여 처리 정밀도 향상

2. **Persona & Safeguard 적용**
   - 페르소나 정의 및 엄격한 Output Format 제약 조건을 설정하여 환각(Hallucination) 현상 방지

3. **Action Item Generation**
   - 최종 추출된 결과를 담당자별, 우선순위별 구조화된 문서(Markdown/JSON) 형태로 자동 출력

---

## 주요 성과 및 인사이트
- 정형화되지 않은 텍스트 데이터를 즉시 실행 가능한 결론으로 자동 변환하여 문서 작성 및 요약 시간 단축
- 시스템 프롬프트 가드레일 설정을 통해 환각률 최소화 및 출력 일관성 확보
- 에이전틱 워크플로우(Agentic Workflow) 설계를 통한 복잡한 추론 문제 해결 역량 검증
