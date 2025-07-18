from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.db import get_db as get_async_session
from src.schemas.admin_user import AdminUserCreate, AdminUserOut
from src.service.admin_user_service import (
    create_admin_user,
    get_all_admins,
    get_admin_by_id,
    delete_admin_by_id
)

router = APIRouter(prefix="/admin", tags=["Admin Users"])

@router.post("/", response_model=AdminUserOut)
async def create_admin(data: AdminUserCreate, session: AsyncSession = Depends(get_async_session)):
    return await create_admin_user(data, session)

@router.get("/", response_model=list[AdminUserOut])
async def read_all_admins(session: AsyncSession = Depends(get_async_session)):
    return await get_all_admins(session)

@router.get("/{admin_id}", response_model=AdminUserOut)
async def read_admin(admin_id: int, session: AsyncSession = Depends(get_async_session)):
    admin = await get_admin_by_id(admin_id, session)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    return admin

@router.delete("/{admin_id}")
async def delete_admin(admin_id: int, session: AsyncSession = Depends(get_async_session)):
    admin = await delete_admin_by_id(admin_id, session)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    return {"detail": "Admin deleted"}
