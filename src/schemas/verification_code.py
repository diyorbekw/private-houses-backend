from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class VerificationCodeBase(BaseModel):
    phone: str
    code: str
    is_verified: Optional[bool] = False
    sent_at: datetime
    expires_at: datetime


class VerificationCodeCreate(VerificationCodeBase):
    pass


class VerificationCodeRead(VerificationCodeBase):
    id: int

    class Config:
        orm_mode = True
