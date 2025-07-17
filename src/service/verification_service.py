from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from datetime import datetime
from src.models.verification_code import VerificationCode
from src.schemas.verification_code import VerificationCodeCreate
from src.service.audit_log_service import AuditLogger

async def create_verification_code(session: AsyncSession, data: VerificationCodeCreate) -> VerificationCode:
    code = VerificationCode(**data.model_dump())
    session.add(code)
    await session.commit()
    await session.refresh(code)
    return code


async def verify_code(session: AsyncSession, phone: str, code: str) -> bool:
    result = await session.execute(
        select(VerificationCode).where(
            VerificationCode.phone == phone,
            VerificationCode.code == code
        )
    )
    code_obj = result.scalar_one_or_none()
    if not code_obj:
        raise HTTPException(status_code=404, detail="Code not found")

    if code_obj.expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Code has expired")

    code_obj.is_verified = True
    await session.commit()
    return True
