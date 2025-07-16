from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class VerificationCodeCreate(BaseModel):
    phone: str
    code: str
    expires_at: datetime


class VerificationCodeResponse(BaseModel):
    id: int
    phone: str
    code: str
    is_verified: bool
    sent_at: datetime
    expires_at: datetime

    class Config:
        orm_mode = True
