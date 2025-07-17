from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.db import get_db as get_session
from src.schemas.verification_code import VerificationCodeCreate
from src.service import verification_service

router = APIRouter(prefix="/verification", tags=["Verification"])


@router.post("/send")
async def send_code(data: VerificationCodeCreate, session: AsyncSession = Depends(get_session)):
    return await verification_service.create_verification_code(session, data)


@router.post("/verify")
async def verify(phone: str, code: str, session: AsyncSession = Depends(get_session)):
    await verification_service.verify_code(session, phone, code)
    return {"detail": "Success Verification"}
