from pydantic import BaseModel


class ImageInfo(BaseModel):
    id: int
    prompt: str
    url: str
    user_id: int

    class Config:
        from_attributes = True
