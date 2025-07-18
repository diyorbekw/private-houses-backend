from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.admin_user import AdminUser
from src.schemas.admin_user import AdminUserCreate
from src.core.security import hash_password
from datetime import datetime

async def create_admin_user(data: AdminUserCreate, session: AsyncSession) -> AdminUser:
    user = AdminUser(
        username=data.username,
        password_hash=hash_password(data.password),
        full_name=data.full_name,
        role=data.role,
        created_at=datetime.utcnow()
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

async def get_all_admins(session: AsyncSession):
    result = await session.execute(select(AdminUser))
    return result.scalars().all()

async def get_admin_by_id(admin_id: int, session: AsyncSession):
    result = await session.execute(select(AdminUser).where(AdminUser.id == admin_id))
    return result.scalar_one_or_none()

async def delete_admin_by_id(admin_id: int, session: AsyncSession):
    admin = await get_admin_by_id(admin_id, session)
    if admin:
        await session.delete(admin)
        await session.commit()
    return admin
