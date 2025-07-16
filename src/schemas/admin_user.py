from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AdminUserCreate(BaseModel):
    username: str
    password: str 
    full_name: str
    role: str  


class AdminUserUpdate(BaseModel):
    password: Optional[str]
    full_name: Optional[str]
    role: Optional[str]


class AdminUserResponse(BaseModel):
    id: int
    username: str
    full_name: str
    role: str
    created_at: datetime

    class Config:
        orm_mode = True
