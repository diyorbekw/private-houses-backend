from pydantic import BaseModel
from typing import Optional


class RegisterData(BaseModel):
    phone_number: str
    password: str
    role_id: Optional[int] = None


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    role_id: int | None = None


class UserResponse(BaseModel):
    id: int
    phone_number: str
    role_id: Optional[int] = None

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    phone_number: Optional[str] = None
    role_id: Optional[int] = None
