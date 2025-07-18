from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.db import get_db as get_session
from src.schemas.resident import ResidentCreate, ResidentUpdate, ResidentResponse
from src.service import resident_service
from src.utils.auth import require_role

router = APIRouter(prefix="/residents", tags=["Residents"])


@router.post("/", response_model=ResidentResponse)
async def create_resident(
    data: ResidentCreate, 
    session: AsyncSession = Depends(get_session),
    current_user = Depends(require_role("admin"))
):
    return await resident_service.create_resident(session, data)


@router.get("/house/{house_id}", response_model=list[ResidentResponse])
async def list_by_house(
    house_id: int, 
    session: AsyncSession = Depends(get_session),
    current_user = Depends(require_role("admin"))
):
    return await resident_service.get_residents_by_house(session, house_id)


@router.put("/{resident_id}", response_model=ResidentResponse)
async def update_resident(
    resident_id: int, 
    data: ResidentUpdate, 
    session: AsyncSession = Depends(get_session),
    current_user = Depends(require_role("admin"))
):
    return await resident_service.update_resident(session, resident_id, data)


@router.delete("/{resident_id}")
async def delete_resident(
    resident_id: int, 
    session: AsyncSession = Depends(get_session),
    current_user = Depends(require_role("admin"))
):
    await resident_service.delete_resident(session, resident_id)
    return {"detail": "Удалено"}
