from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from src.models.house import House
from src.schemas.house import HouseCreate, HouseUpdate
from src.service.audit_log_service import AuditLogger
from src.utils.common import model_to_dict
import uuid


async def create_house(session: AsyncSession, data: HouseCreate, actor_id: int, actor_type: str) -> House:
    house = House(unique_code=uuid.uuid4(), **data.model_dump())
    session.add(house)
    await session.commit()
    await session.refresh(house)

    logger = AuditLogger(session)
    await logger.log(actor_type, actor_id, "create", "House", house.id, None, model_to_dict(house))

    return house


async def get_house(session: AsyncSession, house_id: int) -> House:
    result = await session.execute(select(House).where(House.id == house_id))
    house = result.scalar_one_or_none()
    if not house:
        raise HTTPException(status_code=404, detail="House not found")
    return house


async def update_house(session: AsyncSession, house_id: int, data: HouseUpdate, actor_id: int, actor_type: str) -> House:
    house = await get_house(session, house_id)
    old_data = model_to_dict(house)

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(house, key, value)
    await session.commit()
    await session.refresh(house)

    logger = AuditLogger(session)
    await logger.log(actor_type, actor_id, "update", "House", house.id, old_data, model_to_dict(house))

    return house


async def delete_house(session: AsyncSession, house_id: int, actor_id: int, actor_type: str) -> None:
    house = await get_house(session, house_id)
    old_data = model_to_dict(house)
    await session.delete(house)
    await session.commit()

    logger = AuditLogger(session)
    await logger.log(actor_type, actor_id, "delete", "House", house.id, old_data, None)
