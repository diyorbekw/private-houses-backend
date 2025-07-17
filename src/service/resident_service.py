from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from src.models.resident import Resident
from src.schemas.resident import ResidentCreate, ResidentUpdate
from src.service.audit_log_service import AuditLogger
from src.utils.common import model_to_dict


async def create_resident(session: AsyncSession, data: ResidentCreate, actor_id: int, actor_type: str) -> Resident:
    if data.is_owner:
        result = await session.execute(
            select(Resident).where(Resident.house_id == data.house_id, Resident.is_owner == True)
        )
        existing_owner = result.scalars().first()
        if existing_owner:
            raise HTTPException(status_code=400, detail="This house already has an owner")

    new_resident = Resident(**data.model_dump())
    session.add(new_resident)
    await session.commit()
    await session.refresh(new_resident)

    await AuditLogger(session).log(
        user_type=actor_type,
        user_id=actor_id,
        action="create",
        entity="Resident",
        entity_id=new_resident.id,
        old_value=None,
        new_value=model_to_dict(new_resident)
    )

    return new_resident


async def get_residents_by_house(session: AsyncSession, house_id: int) -> list[Resident]:
    result = await session.execute(
        select(Resident).where(Resident.house_id == house_id)
    )
    return result.scalars().all()


async def update_resident(session: AsyncSession, resident_id: int, data: ResidentUpdate, actor_id: int, actor_type: str) -> Resident:
    result = await session.execute(select(Resident).where(Resident.id == resident_id))
    resident = result.scalar_one_or_none()

    if not resident:
        raise HTTPException(status_code=404, detail="Resident not found")

    old_data = model_to_dict(resident)

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(resident, key, value)

    await session.commit()
    await session.refresh(resident)

    await AuditLogger(session).log(
        user_type=actor_type,
        user_id=actor_id,
        action="update",
        entity="Resident",
        entity_id=resident.id,
        old_value=old_data,
        new_value=model_to_dict(resident)
    )

    return resident


async def delete_resident(session: AsyncSession, resident_id: int, actor_id: int, actor_type: str) -> None:
    result = await session.execute(select(Resident).where(Resident.id == resident_id))
    resident = result.scalar_one_or_none()

    if not resident:
        raise HTTPException(status_code=404, detail="Resident not found")

    old_data = model_to_dict(resident)

    await session.delete(resident)
    await session.commit()

    await AuditLogger(session).log(
        user_type=actor_type,
        user_id=actor_id,
        action="delete",
        entity="Resident",
        entity_id=resident_id,
        old_value=old_data,
        new_value=None
    )
