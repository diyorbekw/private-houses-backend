from pydantic import BaseModel, constr, HttpUrl
from typing import Optional
from datetime import date, datetime


class ResidentBase(BaseModel):
    full_name: str
    birth_date: date
    gender: str
    phone: str
    passport_number: str
    relationship_to_owner: Optional[str] = None
    is_owner: bool = False
    photo_url: Optional[HttpUrl] = None


class ResidentCreate(ResidentBase):
    house_id: int


class ResidentUpdate(ResidentBase):
    pass


class ResidentOut(ResidentBase):
    id: int
    house_id: int
    created_at: datetime

    class Config:
        orm_mode = True
