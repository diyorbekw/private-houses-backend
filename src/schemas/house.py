from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


class HouseCreate(BaseModel):
    street_id: int
    house_number: str
    latitude: Optional[float]
    longitude: Optional[float]
    created_by: int


class HouseUpdate(BaseModel):
    street_id: Optional[int]
    house_number: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]


class HouseResponse(BaseModel):
    id: int
    unique_code: UUID
    street_id: int
    house_number: str
    latitude: Optional[float]
    longitude: Optional[float]
    created_by: int
    created_at: datetime

    class Config:
        orm_mode = True