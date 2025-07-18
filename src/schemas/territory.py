from pydantic import BaseModel
from typing import Optional

class CountryCreate(BaseModel):
    name: str

class CountryUpdate(BaseModel):
    name: Optional[str]

class CountryResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class RegionCreate(BaseModel):
    name: str
    country_id: int

class RegionUpdate(BaseModel):
    name: Optional[str]
    country_id: Optional[int]

class RegionResponse(BaseModel):
    id: int
    name: str
    country_id: int

    class Config:
        from_attributes = True


class CityCreate(BaseModel):
    name: str
    region_id: int

class CityUpdate(BaseModel):
    name: Optional[str]
    region_id: Optional[int]

class CityResponse(BaseModel):
    id: int
    name: str
    region_id: int

    class Config:
        from_attributes = True


class DistrictCreate(BaseModel):
    name: str
    city_id: int

class DistrictUpdate(BaseModel):
    name: Optional[str]
    city_id: Optional[int]

class DistrictResponse(BaseModel):
    id: int
    name: str
    city_id: int

    class Config:
        from_attributes = True


class MicroDistrictCreate(BaseModel):
    name: str
    district_id: int

class MicroDistrictUpdate(BaseModel):
    name: Optional[str]
    district_id: Optional[int]

class MicroDistrictResponse(BaseModel):
    id: int
    name: str
    district_id: int

    class Config:
        from_attributes = True


class StreetCreate(BaseModel):
    name: str
    microdistrict_id: int

class StreetUpdate(BaseModel):
    name: Optional[str]
    microdistrict_id: Optional[int]

class StreetResponse(BaseModel):
    id: int
    name: str
    microdistrict_id: int

    class Config:
        from_attributes = True