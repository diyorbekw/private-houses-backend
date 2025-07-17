from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.db import get_db as get_session
from src.schemas.territory import *
from src.service import territory_service

router = APIRouter(prefix="/territory", tags=["Territory"])


@router.post("/countries", response_model=CountryResponse)
async def create_country(data: CountryCreate, session: AsyncSession = Depends(get_session)):
    return await territory_service.create_country(session, data)


@router.post("/regions", response_model=RegionResponse)
async def create_region(data: RegionCreate, session: AsyncSession = Depends(get_session)):
    return await territory_service.create_region(session, data)


@router.get("/regions", response_model=list[RegionResponse])
async def get_regions(country_id: int, session: AsyncSession = Depends(get_session)):
    return await territory_service.get_regions_by_country(session, country_id)


@router.post("/cities", response_model=CityResponse)
async def create_city(data: CityCreate, session: AsyncSession = Depends(get_session)):
    return await territory_service.create_city(session, data)


@router.get("/cities", response_model=list[CityResponse])
async def get_cities(region_id: int, session: AsyncSession = Depends(get_session)):
    return await territory_service.get_cities_by_region(session, region_id)


@router.post("/districts", response_model=DistrictResponse)
async def create_district(data: DistrictCreate, session: AsyncSession = Depends(get_session)):
    return await territory_service.create_district(session, data)


@router.get("/districts", response_model=list[DistrictResponse])
async def get_districts(city_id: int, session: AsyncSession = Depends(get_session)):
    return await territory_service.get_districts_by_city(session, city_id)


@router.post("/microdistricts", response_model=MicroDistrictResponse)
async def create_microdistrict(data: MicroDistrictCreate, session: AsyncSession = Depends(get_session)):
    return await territory_service.create_microdistrict(session, data)


@router.get("/microdistricts", response_model=list[MicroDistrictResponse])
async def get_microdistricts(district_id: int, session: AsyncSession = Depends(get_session)):
    return await territory_service.get_microdistricts_by_district(session, district_id)


@router.post("/streets", response_model=StreetResponse)
async def create_street(data: StreetCreate, session: AsyncSession = Depends(get_session)):
    return await territory_service.create_street(session, data)


@router.get("/streets", response_model=list[StreetResponse])
async def get_streets(microdistrict_id: int, session: AsyncSession = Depends(get_session)):
    return await territory_service.get_streets_by_microdistrict(session, microdistrict_id)
