from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.house import HouseCreate, HouseOut, HouseUpdate
from src.service.house_service import (
    create_house,
    get_house_by_id,
    get_all_houses,
    update_house,
    delete_house
)
from src.core.db import get_db as get_session

router = APIRouter(prefix="/house", tags=["House"])

@router.post("/", response_model=HouseOut)
async def create(house: HouseCreate, session: AsyncSession = Depends(get_session)):
    return await create_house(session, house)

@router.get("/{house_id}", response_model=HouseOut)
async def get_by_id(house_id: int, session: AsyncSession = Depends(get_session)):
    house = await get_house_by_id(session, house_id)
    if not house:
        raise HTTPException(status_code=404, detail="House not found")
    return house

@router.get("/", response_model=list[HouseOut])
async def get_all(session: AsyncSession = Depends(get_session)):
    return await get_all_houses(session)

@router.put("/{house_id}", response_model=HouseOut)
async def update(house_id: int, house: HouseUpdate, session: AsyncSession = Depends(get_session)):
    updated = await update_house(session, house_id, house)
    if not updated:
        raise HTTPException(status_code=404, detail="House not found")
    return updated

@router.delete("/{house_id}")
async def delete(house_id: int, session: AsyncSession = Depends(get_session)):
    success = await delete_house(session, house_id)
    if not success:
        raise HTTPException(status_code=404, detail="House not found")
    return {"message": "House deleted"}
