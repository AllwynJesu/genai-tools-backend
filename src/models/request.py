from pydantic import BaseModel, Field, field_validator

from models.tools_action import Actions

class RequestData(BaseModel):
    action: Actions = Field(frozen=True, description="The action to be performed")
    page_url: str = Field(frozen=True, description="The URL of the page to be processed")
    input_text: str = Field(default="", frozen=True,description="The selected text (optional)")
    chat_message: str = Field(default="", frozen=True, description="The chat message (optional)")

    @field_validator("action")
    def action_must_be_valid(cls, v):
        if v not in Actions:
            raise ValueError(f"Invalid action: {v}. Valid actions are: {', '.join(Actions.keys())}")
        return v
