from pydantic import BaseModel


class PostResponse(BaseModel):
    id: int
    user_id: int
    content: str


class PostCreate(BaseModel):
    content: str


class PostUpdate(BaseModel):
    content: str


class PostContent(BaseModel):
    content: str
