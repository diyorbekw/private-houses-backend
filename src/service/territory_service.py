from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update as sql_update, delete as sql_delete
from src.models.territory import (
    Country, Region, City, District, MicroDistrict, Street
)


# ——— Country ———
async def create_country(db: AsyncSession, data):
    item = Country(**data.dict())
    db.add(item)
    await db.commit(); await db.refresh(item)
    return item

async def get_country(db, item_id): return (await db.execute(select(Country).where(Country.id == item_id))).scalar_one_or_none()
async def get_countrys(db): return (await db.execute(select(Country))).scalars().all()
async def update_country(db, item_id, data):
    await db.execute(sql_update(Country).where(Country.id == item_id).values(**data.dict(exclude_unset=True)))
    await db.commit()
    return await get_country(db, item_id)
async def delete_country(db, item_id):
    await db.execute(sql_delete(Country).where(Country.id == item_id))
    await db.commit()


# ——— Region ———
async def create_region(db, data):
    item = Region(**data.dict()); db.add(item)
    await db.commit(); await db.refresh(item); return item

async def get_region(db, item_id): return (await db.execute(select(Region).where(Region.id == item_id))).scalar_one_or_none()
async def get_regions(db): return (await db.execute(select(Region))).scalars().all()
async def update_region(db, item_id, data):
    await db.execute(sql_update(Region).where(Region.id == item_id).values(**data.dict(exclude_unset=True)))
    await db.commit(); return await get_region(db, item_id)
async def delete_region(db, item_id):
    await db.execute(sql_delete(Region).where(Region.id == item_id))
    await db.commit()


# ——— City ———
async def create_city(db, data):
    item = City(**data.dict()); db.add(item)
    await db.commit(); await db.refresh(item); return item

async def get_city(db, item_id): return (await db.execute(select(City).where(City.id == item_id))).scalar_one_or_none()
async def get_citys(db): return (await db.execute(select(City))).scalars().all()
async def update_city(db, item_id, data):
    await db.execute(sql_update(City).where(City.id == item_id).values(**data.dict(exclude_unset=True)))
    await db.commit(); return await get_city(db, item_id)
async def delete_city(db, item_id):
    await db.execute(sql_delete(City).where(City.id == item_id))
    await db.commit()


# ——— District ———
async def create_district(db, data):
    item = District(**data.dict()); db.add(item)
    await db.commit(); await db.refresh(item); return item

async def get_district(db, item_id): return (await db.execute(select(District).where(District.id == item_id))).scalar_one_or_none()
async def get_districts(db): return (await db.execute(select(District))).scalars().all()
async def update_district(db, item_id, data):
    await db.execute(sql_update(District).where(District.id == item_id).values(**data.dict(exclude_unset=True)))
    await db.commit(); return await get_district(db, item_id)
async def delete_district(db, item_id):
    await db.execute(sql_delete(District).where(District.id == item_id))
    await db.commit()


# ——— MicroDistrict ———
async def create_microdistrict(db, data):
    item = MicroDistrict(**data.dict()); db.add(item)
    await db.commit(); await db.refresh(item); return item

async def get_microdistrict(db, item_id): return (await db.execute(select(MicroDistrict).where(MicroDistrict.id == item_id))).scalar_one_or_none()
async def get_microdistricts(db): return (await db.execute(select(MicroDistrict))).scalars().all()
async def update_microdistrict(db, item_id, data):
    await db.execute(sql_update(MicroDistrict).where(MicroDistrict.id == item_id).values(**data.dict(exclude_unset=True)))
    await db.commit(); return await get_microdistrict(db, item_id)
async def delete_microdistrict(db, item_id):
    await db.execute(sql_delete(MicroDistrict).where(MicroDistrict.id == item_id))
    await db.commit()


# ——— Street ———
async def create_street(db, data):
    item = Street(**data.dict()); db.add(item)
    await db.commit(); await db.refresh(item); return item

async def get_street(db, item_id): return (await db.execute(select(Street).where(Street.id == item_id))).scalar_one_or_none()
async def get_streets(db): return (await db.execute(select(Street))).scalars().all()
async def update_street(db, item_id, data):
    await db.execute(sql_update(Street).where(Street.id == item_id).values(**data.dict(exclude_unset=True)))
    await db.commit(); return await get_street(db, item_id)
async def delete_street(db, item_id):
    await db.execute(sql_delete(Street).where(Street.id == item_id))
    await db.commit()
