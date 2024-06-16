from fastapi import APIRouter, HTTPException

from models.request import RequestData
from models.response import ChatWithAIResponse, RewriteResponse, SummaryResponse

tools_router = APIRouter(
    prefix="/tools",
)

@tools_router.post("/summary", response_model=SummaryResponse)
def get_summary(request: RequestData):
    return {"summary": "This is a summary", "page_url": request.page_url}

@tools_router.post("/rewrite", response_model=RewriteResponse)
def rewrite(request: RequestData):
    return {"rewrite": "This is a new text", "page_url": request.page_url, "original_text": request.input_text}

@tools_router.post("/chat-ai", response_model=ChatWithAIResponse)
def chat_with_ai(request: RequestData):
    return {"response": "Hi from AI", "chat_message": request.chat_message}