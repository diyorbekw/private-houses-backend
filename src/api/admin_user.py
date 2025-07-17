from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.db import get_db as get_session
from src.schemas.admin_user import AdminUserCreate, AdminUserUpdate, AdminUserResponse
from src.service import admin_user_service

router = APIRouter(prefix="/admin", tags=["Admin Users"])


@router.post("/", response_model=AdminUserResponse)
async def create_admin(data: AdminUserCreate, session: AsyncSession = Depends(get_session)):
    return await admin_user_service.create_admin(session, data)
