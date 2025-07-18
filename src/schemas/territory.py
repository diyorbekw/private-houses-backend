from pydantic import BaseModel
from typing import Optional, List


# ——— Country ———
class CountryBase(BaseModel):
    name: str

class CountryCreate(CountryBase):
    pass

class CountryUpdate(CountryBase):
    pass

class CountryRead(CountryBase):
    id: int
    class Config:
        orm_mode = True


# ——— Region ———
class RegionBase(BaseModel):
    name: str
    country_id: int

class RegionCreate(RegionBase):
    pass

class RegionUpdate(BaseModel):
    name: Optional[str]
    country_id: Optional[int]

class RegionRead(RegionBase):
    id: int
    country: Optional[CountryRead]
    class Config:
        orm_mode = True


# ——— City ———
class CityBase(BaseModel):
    name: str
    region_id: int

class CityCreate(CityBase):
    pass

class CityUpdate(BaseModel):
    name: Optional[str]
    region_id: Optional[int]

class CityRead(CityBase):
    id: int
    region: Optional[RegionRead]
    class Config:
        orm_mode = True


# ——— District ———
class DistrictBase(BaseModel):
    name: str
    city_id: int

class DistrictCreate(DistrictBase):
    pass

class DistrictUpdate(BaseModel):
    name: Optional[str]
    city_id: Optional[int]

class DistrictRead(DistrictBase):
    id: int
    city: Optional[CityRead]
    class Config:
        orm_mode = True


# ——— MicroDistrict ———
class MicroDistrictBase(BaseModel):
    name: str
    district_id: int

class MicroDistrictCreate(MicroDistrictBase):
    pass

class MicroDistrictUpdate(BaseModel):
    name: Optional[str]
    district_id: Optional[int]

class MicroDistrictRead(MicroDistrictBase):
    id: int
    district: Optional[DistrictRead]
    class Config:
        orm_mode = True


# ——— Street ———
class StreetBase(BaseModel):
    name: str
    microdistrict_id: int

class StreetCreate(StreetBase):
    pass

class StreetUpdate(BaseModel):
    name: Optional[str]
    microdistrict_id: Optional[int]

class StreetRead(StreetBase):
    id: int
    microdistrict: Optional[MicroDistrictRead]
    class Config:
        orm_mode = True
