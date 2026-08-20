from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import MeetingSummaryAgent
import uvicorn

app = FastAPI(
    title="Enterprise RAG Agent API",
    description="AWS Bedrock 기반 회의록 요약 및 Action Item 추출 API",
    version="1.0.0"
)

agent = MeetingSummaryAgent()


class MeetingRequest(BaseModel):
    transcript: str
    query: str = "액션 아이템 및 주요 결정사항"


@app.post("/api/summarize")
async def summarize_meeting(request: MeetingRequest):
    try:
        result, retrieved_chunks, is_mock, error = agent.process_transcript(request.transcript, request.query)

        return {
            "status": "success",
            "query": request.query,
            "retrieved_chunks_count": len(retrieved_chunks),
            "used_mock": is_mock,
            "metrics": agent.last_metrics,
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"에이전트 처리 중 오류 발생: {str(e)}")