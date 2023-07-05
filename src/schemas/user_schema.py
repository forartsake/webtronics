from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class UserLogin(UserBase):
    password: str
    username: str
    email: Optional[str] = None


class User(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    is_verified: bool
    role: str

    class Config:
        orm_mode = True
