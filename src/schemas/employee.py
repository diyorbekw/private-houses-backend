from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class EmployeeCreate(BaseModel):
    full_name: str
    phone: str = Field(..., min_length=7, max_length=20)
    telegram_user_id: Optional[int] = None
    region_id: int


class EmployeeUpdate(BaseModel):
    full_name: Optional[str]
    phone: Optional[str]
    telegram_user_id: Optional[int]
    region_id: Optional[int]
    is_active: Optional[bool]


class EmployeeOut(BaseModel):
    id: int
    full_name: str
    phone: str
    telegram_user_id: Optional[int]
    region_id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True
