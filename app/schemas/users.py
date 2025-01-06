from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    age: int = Field(..., gt=0, lt=130)




class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    age: int

    class Config:
        orm_mode = True