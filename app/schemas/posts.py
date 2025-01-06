from pydantic import BaseModel, Field
from datetime import datetime

class PostCreate(BaseModel):
    title: str = Field(..., max_length=50)
    body: str = Field(..., max_length=500)
    user_id: int

class PostResponse(BaseModel):
    id: int
    title: str
    body: str
    created_at: datetime
    modified_at: datetime
    user_id: int

    class Config:
        orm_mode = True
