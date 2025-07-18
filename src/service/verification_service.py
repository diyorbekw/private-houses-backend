from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.verification_code import VerificationCode
from src.schemas.verification_code import VerificationCodeCreate


async def create_verification_code(db: AsyncSession, data: VerificationCodeCreate):
    new_code = VerificationCode(**data.dict())
    db.add(new_code)
    await db.commit()
    await db.refresh(new_code)
    return new_code


async def get_verification_codes(db: AsyncSession):
    result = await db.execute(select(VerificationCode))
    return result.scalars().all()
