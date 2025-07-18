from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class EmployeeCreate(BaseModel):
    full_name: str
    phone: str
    telegram_user_id: Optional[int]
    region_id: Optional[int]


class EmployeeUpdate(BaseModel):
    full_name: Optional[str]
    phone: Optional[str]
    telegram_user_id: Optional[int]
    region_id: Optional[int]
    is_active: Optional[bool]


class EmployeeResponse(BaseModel):
    id: int
    full_name: str
    phone: str
    telegram_user_id: Optional[int]
    region_id: Optional[int]
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True
