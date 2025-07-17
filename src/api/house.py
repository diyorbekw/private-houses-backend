from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.db import get_db as get_session
from src.schemas.house import HouseCreate, HouseUpdate, HouseResponse
from src.service import house_service

router = APIRouter(prefix="/houses", tags=["Houses"])


@router.post("/", response_model=HouseResponse)
async def create_house(data: HouseCreate, session: AsyncSession = Depends(get_session)):
    return await house_service.create_house(session, data)


@router.get("/{house_id}", response_model=HouseResponse)
async def get_house(house_id: int, session: AsyncSession = Depends(get_session)):
    return await house_service.get_house(session, house_id)


@router.put("/{house_id}", response_model=HouseResponse)
async def update_house(house_id: int, data: HouseUpdate, session: AsyncSession = Depends(get_session)):
    return await house_service.update_house(session, house_id, data)


@router.delete("/{house_id}")
async def delete_house(house_id: int, session: AsyncSession = Depends(get_session)):
    await house_service.delete_house(session, house_id)
    return {"detail": "Удалено"}
