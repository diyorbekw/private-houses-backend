from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.resident import ResidentCreate, ResidentOut, ResidentUpdate
from src.service.resident_service import (
    create_resident, get_resident_by_id, get_all_residents,
    update_resident, delete_resident
)
from src.core.db import get_db as get_session

router = APIRouter(prefix="/residents", tags=["Residents"])


@router.post("", response_model=ResidentOut)
async def create(data: ResidentCreate, session: AsyncSession = Depends(get_session)):
    return await create_resident(session, data)


@router.get("/{resident_id}", response_model=ResidentOut)
async def get_by_id(resident_id: int, session: AsyncSession = Depends(get_session)):
    resident = await get_resident_by_id(session, resident_id)
    if not resident:
        raise HTTPException(status_code=404, detail="Resident not found")
    return resident


@router.get("", response_model=list[ResidentOut])
async def get_all(session: AsyncSession = Depends(get_session)):
    return await get_all_residents(session)


@router.put("/{resident_id}", response_model=ResidentOut)
async def update(resident_id: int, data: ResidentUpdate, session: AsyncSession = Depends(get_session)):
    updated = await update_resident(session, resident_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Resident not found")
    return updated


@router.delete("/{resident_id}")
async def delete(resident_id: int, session: AsyncSession = Depends(get_session)):
    await delete_resident(session, resident_id)
    return {"detail": "Resident deleted"}
