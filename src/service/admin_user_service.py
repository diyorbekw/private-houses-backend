from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from src.models.admin_user import AdminUser
from src.schemas.admin_user import AdminUserCreate, AdminUserUpdate
from src.service.audit_log_service import AuditLogger
from src.utils.common import model_to_dict
import hashlib


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


async def create_admin(session: AsyncSession, data: AdminUserCreate, actor_id: int) -> AdminUser:
    new_admin = AdminUser(
        username=data.username,
        full_name=data.full_name,
        role=data.role,
        password_hash=hash_password(data.password)
    )
    session.add(new_admin)
    await session.commit()
    await session.refresh(new_admin)

    logger = AuditLogger(session)
    await logger.log(
        user_type="admin",
        user_id=actor_id,
        action="create",
        entity="AdminUser",
        entity_id=new_admin.id,
        old_value=None,
        new_value=model_to_dict(new_admin)
    )
    return new_admin


async def get_admin_by_username(session: AsyncSession, username: str) -> AdminUser:
    result = await session.execute(select(AdminUser).where(AdminUser.username == username))
    return result.scalar_one_or_none()


async def update_admin(session: AsyncSession, admin_id: int, data: AdminUserUpdate, actor_id: int) -> AdminUser:
    result = await session.execute(select(AdminUser).where(AdminUser.id == admin_id))
    admin = result.scalar_one_or_none()
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    old_data = model_to_dict(admin)

    if data.password:
        admin.password_hash = hash_password(data.password)
    if data.full_name:
        admin.full_name = data.full_name
    if data.role:
        admin.role = data.role

    await session.commit()
    await session.refresh(admin)

    logger = AuditLogger(session)
    await logger.log(
        user_type="admin",
        user_id=actor_id,
        action="update",
        entity="AdminUser",
        entity_id=admin.id,
        old_value=old_data,
        new_value=model_to_dict(admin)
    )

    return admin