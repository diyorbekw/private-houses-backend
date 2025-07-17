from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from src.models.territory import Country, Region, City, District, MicroDistrict, Street
from src.schemas.territory import (
    CountryCreate, CountryUpdate,
    RegionCreate, RegionUpdate,
    CityCreate, CityUpdate,
    DistrictCreate, DistrictUpdate,
    MicroDistrictCreate, MicroDistrictUpdate,
    StreetCreate, StreetUpdate
)
from src.service.audit_log_service import AuditLogger
from src.utils.common import model_to_dict

# --- COUNTRY ---
async def create_country(session: AsyncSession, data: CountryCreate, actor_id: int, actor_type: str) -> Country:
    country = Country(**data.model_dump())
    session.add(country)
    await session.commit()
    await session.refresh(country)

    await AuditLogger(session).log(
        user_type=actor_type,
        user_id=actor_id,
        action="create",
        entity="Country",
        entity_id=country.id,
        old_value=None,
        new_value=model_to_dict(country)
    )
    return country


async def update_country(session: AsyncSession, country_id: int, data: CountryUpdate, actor_id: int, actor_type: str) -> Country:
    result = await session.execute(select(Country).where(Country.id == country_id))
    country = result.scalar_one_or_none()
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")

    old_data = model_to_dict(country)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(country, key, value)

    await session.commit()
    await session.refresh(country)

    await AuditLogger(session).log(
        user_type=actor_type,
        user_id=actor_id,
        action="update",
        entity="Country",
        entity_id=country.id,
        old_value=old_data,
        new_value=model_to_dict(country)
    )
    return country


# --- REGION ---
async def create_region(session: AsyncSession, data: RegionCreate, actor_id: int, actor_type: str) -> Region:
    region = Region(**data.model_dump())
    session.add(region)
    await session.commit()
    await session.refresh(region)

    await AuditLogger(session).log(
        user_type=actor_type,
        user_id=actor_id,
        action="create",
        entity="Region",
        entity_id=region.id,
        old_value=None,
        new_value=model_to_dict(region)
    )
    return region


async def get_regions_by_country(session: AsyncSession, country_id: int) -> list[Region]:
    result = await session.execute(select(Region).where(Region.country_id == country_id))
    return result.scalars().all()


async def update_region(session: AsyncSession, region_id: int, data: RegionUpdate, actor_id: int, actor_type: str) -> Region:
    result = await session.execute(select(Region).where(Region.id == region_id))
    region = result.scalar_one_or_none()
    if not region:
        raise HTTPException(status_code=404, detail="Region not found")

    old_data = model_to_dict(region)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(region, key, value)

    await session.commit()
    await session.refresh(region)

    await AuditLogger(session).log(
        user_type=actor_type,
        user_id=actor_id,
        action="update",
        entity="Region",
        entity_id=region.id,
        old_value=old_data,
        new_value=model_to_dict(region)
    )
    return region


# --- CITY ---
async def create_city(session: AsyncSession, data: CityCreate, actor_id: int, actor_type: str) -> City:
    city = City(**data.model_dump())
    session.add(city)
    await session.commit()
    await session.refresh(city)

    await AuditLogger(session).log(
        user_type=actor_type,
        user_id=actor_id,
        action="create",
        entity="City",
        entity_id=city.id,
        old_value=None,
        new_value=model_to_dict(city)
    )
    return city


async def get_cities_by_region(session: AsyncSession, region_id: int) -> list[City]:
    result = await session.execute(select(City).where(City.region_id == region_id))
    return result.scalars().all()


async def update_city(session: AsyncSession, city_id: int, data: CityUpdate, actor_id: int, actor_type: str) -> City:
    result = await session.execute(select(City).where(City.id == city_id))
    city = result.scalar_one_or_none()
    if not city:
        raise HTTPException(status_code=404, detail="City not found")

    old_data = model_to_dict(city)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(city, key, value)

    await session.commit()
    await session.refresh(city)

    await AuditLogger(session).log(
        user_type=actor_type,
        user_id=actor_id,
        action="update",
        entity="City",
        entity_id=city.id,
        old_value=old_data,
        new_value=model_to_dict(city)
    )
    return city


# --- DISTRICT ---
async def create_district(session: AsyncSession, data: DistrictCreate, actor_id: int, actor_type: str) -> District:
    district = District(**data.model_dump())
    session.add(district)
    await session.commit()
    await session.refresh(district)

    await AuditLogger(session).log(
        user_type=actor_type,
        user_id=actor_id,
        action="create",
        entity="District",
        entity_id=district.id,
        old_value=None,
        new_value=model_to_dict(district)
    )
    return district


async def get_districts_by_city(session: AsyncSession, city_id: int) -> list[District]:
    result = await session.execute(select(District).where(District.city_id == city_id))
    return result.scalars().all()


async def update_district(session: AsyncSession, district_id: int, data: DistrictUpdate, actor_id: int, actor_type: str) -> District:
    result = await session.execute(select(District).where(District.id == district_id))
    district = result.scalar_one_or_none()
    if not district:
        raise HTTPException(status_code=404, detail="District not found")

    old_data = model_to_dict(district)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(district, key, value)

    await session.commit()
    await session.refresh(district)

    await AuditLogger(session).log(
        user_type=actor_type,
        user_id=actor_id,
        action="update",
        entity="District",
        entity_id=district.id,
        old_value=old_data,
        new_value=model_to_dict(district)
    )
    return district


# --- MICRODISTRICT ---
async def create_microdistrict(session: AsyncSession, data: MicroDistrictCreate, actor_id: int, actor_type: str) -> MicroDistrict:
    md = MicroDistrict(**data.model_dump())
    session.add(md)
    await session.commit()
    await session.refresh(md)

    await AuditLogger(session).log(
        user_type=actor_type,
        user_id=actor_id,
        action="create",
        entity="MicroDistrict",
        entity_id=md.id,
        old_value=None,
        new_value=model_to_dict(md)
    )
    return md


async def get_microdistricts_by_district(session: AsyncSession, district_id: int) -> list[MicroDistrict]:
    result = await session.execute(select(MicroDistrict).where(MicroDistrict.district_id == district_id))
    return result.scalars().all()


async def update_microdistrict(session: AsyncSession, md_id: int, data: MicroDistrictUpdate, actor_id: int, actor_type: str) -> MicroDistrict:
    result = await session.execute(select(MicroDistrict).where(MicroDistrict.id == md_id))
    md = result.scalar_one_or_none()
    if not md:
        raise HTTPException(status_code=404, detail="MicroDistrict not found")

    old_data = model_to_dict(md)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(md, key, value)

    await session.commit()
    await session.refresh(md)

    await AuditLogger(session).log(
        user_type=actor_type,
        user_id=actor_id,
        action="update",
        entity="MicroDistrict",
        entity_id=md.id,
        old_value=old_data,
        new_value=model_to_dict(md)
    )
    return md


# --- STREET ---
async def create_street(session: AsyncSession, data: StreetCreate, actor_id: int, actor_type: str) -> Street:
    street = Street(**data.model_dump())
    session.add(street)
    await session.commit()
    await session.refresh(street)

    await AuditLogger(session).log(
        user_type=actor_type,
        user_id=actor_id,
        action="create",
        entity="Street",
        entity_id=street.id,
        old_value=None,
        new_value=model_to_dict(street)
    )
    return street


async def get_streets_by_microdistrict(session: AsyncSession, microdistrict_id: int) -> list[Street]:
    result = await session.execute(select(Street).where(Street.microdistrict_id == microdistrict_id))
    return result.scalars().all()


async def update_street(session: AsyncSession, street_id: int, data: StreetUpdate, actor_id: int, actor_type: str) -> Street:
    result = await session.execute(select(Street).where(Street.id == street_id))
    street = result.scalar_one_or_none()
    if not street:
        raise HTTPException(status_code=404, detail="Street not found")

    old_data = model_to_dict(street)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(street, key, value)

    await session.commit()
    await session.refresh(street)

    await AuditLogger(session).log(
        user_type=actor_type,
        user_id=actor_id,
        action="update",
        entity="Street",
        entity_id=street.id,
        old_value=old_data,
        new_value=model_to_dict(street)
    )
    return street
