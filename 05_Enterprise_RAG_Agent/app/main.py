from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import MeetingsSummaryAgent
import uvicorn

app = FastAPI(
    title="Enterprise RAG Agent API",
    description="AWS Bedrock 기반 회의록 요약 및 Action Item 추출 API",
    version="1.0.0"
)

agent = MeetingsSummaryAgent()

class MeetingRequest(BaseModel):
    transcript: str
    query: str = "액션 아이템 및 주요 결정사항"

@app.post("/api/summarize")
async def summarize_meeting(request: MeetingRequest):
    try:
        chunks = agent.retrieve_relevant_chunks(request.transcript, request.query)
        
        prompt = agent._build_rag_prompt(chunks, request.query)
        
        return {
            "status": "success",
            "query": request.query,
            "retrieved_chunks_count": len(chunks),
            "message": "Bedrock LLM 연결 로직을 여기에 추가하세요."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"에이전트 처리 중 오류 발생: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)