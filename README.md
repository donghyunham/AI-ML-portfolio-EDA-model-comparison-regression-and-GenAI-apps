# AI & Machine Learning Project Portfolio

> 데이터 탐색(EDA)부터 머신러닝 모델 비교·회귀 예측, 그리고 최신 생성형 AI(RAG & Agent) 애플리케이션 개발까지의 기술 역량을 정돈한 포트폴리오 저장소입니다.

---

## Profile & Tech Stack

### Core & Data Science
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)

### Machine Learning & GenAI
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![AWS Bedrock](https://img.shields.io/badge/AWS_Bedrock-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Generative AI](https://img.shields.io/badge/Generative_AI-412991?style=for-the-badge&logo=openai&logoColor=white)

### Tools & Environment
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

---

### 💡 Core Architecture (Enterprise RAG Agent)

```mermaid
graph LR
    User([User Request]) --> Agent[AWS Bedrock Agent]
    Agent --> VectorDB[(Knowledge Base / Vector DB)]
    VectorDB --> Context[Retrieved Context]
    Context --> LLM[LLM / Claude 3]
    LLM --> Action[Summary & Action Items]
