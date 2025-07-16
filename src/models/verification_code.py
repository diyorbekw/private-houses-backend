from sqlalchemy import Column, Integer, Text, Boolean, TIMESTAMP
from src.core.db import Base

class VerificationCode(Base):
    __tablename__ = "verification_code"
    id = Column(Integer, primary_key=True)
    phone = Column(Text)
    code = Column(Text)
    is_verified = Column(Boolean, default=False)
    sent_at = Column(TIMESTAMP)
    expires_at = Column(TIMESTAMP)
