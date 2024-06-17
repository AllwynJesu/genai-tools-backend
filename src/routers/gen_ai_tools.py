from fastapi import APIRouter, HTTPException

from models.request import RequestData
from models.response import ChatWithAIResponse, RewriteResponse, SummaryResponse, ExtractImportantDetailsResponse
from core import get_summary, get_rewrite, extract_important_details

tools_router = APIRouter(
    prefix="/tools",
)

@tools_router.post("/summary", response_model=SummaryResponse)
def summary(request: RequestData):
    return get_summary(request)

@tools_router.post("/rewrite", response_model=RewriteResponse)
def rewrite(request: RequestData):
    return get_rewrite(request)

@tools_router.post("/chat-ai", response_model=ChatWithAIResponse)
def chat_with_ai(request: RequestData):
    return {"response": "Hi from AI", "chat_message": request.chat_message}

@tools_router.post("/extract-details", response_model=ExtractImportantDetailsResponse)
def extract_details(request: RequestData):
    return extract_important_details(request)