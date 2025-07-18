from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from src.models.resident import Resident
from src.schemas.resident import ResidentCreate, ResidentUpdate


async def create_resident(session: AsyncSession, data: ResidentCreate) -> Resident:
    resident = Resident(**data.dict())
    session.add(resident)
    await session.commit()
    await session.refresh(resident)
    return resident


async def get_resident_by_id(session: AsyncSession, resident_id: int) -> Resident:
    result = await session.execute(select(Resident).where(Resident.id == resident_id))
    return result.scalar_one_or_none()


async def get_all_residents(session: AsyncSession) -> list[Resident]:
    result = await session.execute(select(Resident))
    return result.scalars().all()


async def update_resident(session: AsyncSession, resident_id: int, data: ResidentUpdate) -> Resident:
    await session.execute(
        update(Resident)
        .where(Resident.id == resident_id)
        .values(**data.dict())
    )
    await session.commit()
    return await get_resident_by_id(session, resident_id)


async def delete_resident(session: AsyncSession, resident_id: int) -> None:
    await session.execute(delete(Resident).where(Resident.id == resident_id))
    await session.commit()
