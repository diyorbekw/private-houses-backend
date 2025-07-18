from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.house import House
from src.schemas.house import HouseCreate, HouseUpdate

async def create_house(session: AsyncSession, house_data: HouseCreate) -> House:
    new_house = House(**house_data.dict())
    session.add(new_house)
    await session.commit()
    await session.refresh(new_house)
    return new_house

async def get_house_by_id(session: AsyncSession, house_id: int) -> House:
    result = await session.execute(select(House).where(House.id == house_id))
    return result.scalars().first()

async def get_all_houses(session: AsyncSession) -> list[House]:
    result = await session.execute(select(House))
    return result.scalars().all()

async def update_house(session: AsyncSession, house_id: int, house_data: HouseUpdate) -> House:
    house = await get_house_by_id(session, house_id)
    if not house:
        return None
    for key, value in house_data.dict(exclude_unset=True).items():
        setattr(house, key, value)
    await session.commit()
    await session.refresh(house)
    return house

async def delete_house(session: AsyncSession, house_id: int) -> bool:
    house = await get_house_by_id(session, house_id)
    if not house:
        return False
    await session.delete(house)
    await session.commit()
    return True
