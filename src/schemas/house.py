from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional
from datetime import datetime

class HouseBase(BaseModel):
    street_id: int
    house_number: str
    latitude: float
    longitude: float
    created_by: int

class HouseCreate(HouseBase):
    pass

class HouseUpdate(BaseModel):
    street_id: Optional[int] = None
    house_number: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class HouseOut(BaseModel):
    id: int
    unique_code: UUID
    street_id: int
    house_number: str
    latitude: float
    longitude: float
    created_by: int
    created_at: datetime

    class Config:
        orm_mode = True
