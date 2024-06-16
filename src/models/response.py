from pydantic import BaseModel, Field, field_validator

from models.tools_action import Actions

class SummaryResponse(BaseModel):
    action: Actions = Actions.SUMMARIZE
    page_url: str = Field(frozen=True, description="The URL of the page")
    summary: str = Field(frozen=True, description="The summary of the page")

class RewriteResponse(BaseModel):
    action: Actions = Actions.REWRITE
    page_url: str = Field(frozen=True, description="The URL of the page")
    original_text: str = Field(frozen=True, description="The original text")
    rewrite: str = Field(frozen=True, description="The rewritten text")

class ChatWitDocResponse(BaseModel):
    action: Actions = Actions.CHAT_WITH_DOC
    chat_message: str = Field(frozen=True, description="The user's chat message")
    response: str = Field(frozen=True, description="The response from the AI")

class ChatWithAIResponse(BaseModel):
    action: Actions = Actions.CHAT_WITH_AI
    chat_message: str = Field(frozen=True, description="The user's chat message")
    response: str = Field(frozen=True, description="The response from the AI")