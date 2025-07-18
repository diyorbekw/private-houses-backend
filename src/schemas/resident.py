from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class ResidentCreate(BaseModel):
    house_id: int
    full_name: str
    birth_date: date
    gender: str 
    phone: str
    passport_number: Optional[str]
    relationship_to_owner: Optional[str]
    is_owner: Optional[bool] = False
    photo_url: Optional[str]


class ResidentUpdate(BaseModel):
    full_name: Optional[str]
    birth_date: Optional[date]
    gender: Optional[str]
    phone: Optional[str]
    passport_number: Optional[str]
    relationship_to_owner: Optional[str]
    is_owner: Optional[bool]
    photo_url: Optional[str]


class ResidentResponse(BaseModel):
    id: int
    house_id: int
    full_name: str
    birth_date: date
    gender: str
    phone: str
    passport_number: Optional[str]
    relationship_to_owner: Optional[str]
    is_owner: bool
    photo_url: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
