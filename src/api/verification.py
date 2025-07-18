from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.db import get_db
from src.schemas.verification_code import VerificationCodeCreate, VerificationCodeRead
import src.service.verification_service as svc

router = APIRouter(prefix="/verification-codes", tags=["Verification Code"])


@router.post("/", response_model=VerificationCodeRead)
async def create_verification_code(data: VerificationCodeCreate, db: AsyncSession = Depends(get_db)):
    return await svc.create_verification_code(db, data)


@router.get("/", response_model=list[VerificationCodeRead])
async def list_verification_codes(db: AsyncSession = Depends(get_db)):
    return await svc.get_verification_codes(db)
