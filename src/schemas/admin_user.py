from pydantic import BaseModel
from typing import Literal
from datetime import datetime


class AdminUserCreate(BaseModel):
    username: str
    password: str
    full_name: str
    role: Literal["admin", "supervisor"]


class AdminUserOut(BaseModel):
    id: int
    username: str
    full_name: str
    role: Literal["admin", "supervisor"]
    created_at: datetime

    class Config:
        orm_mode = True
