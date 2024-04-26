from pydantic import BaseModel


class PromptMessage(BaseModel):
    prompt: str
    client_source: str
    user_id: str

    class Config:
        from_attributes = True
