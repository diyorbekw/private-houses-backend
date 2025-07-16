from sqlalchemy import Column, Integer, Text, BigInteger, ForeignKey, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from src.core.db import Base

class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    full_name = Column(Text)
    phone = Column(Text, unique=True)
    telegram_user_id = Column(BigInteger)
    region_id = Column(Integer, ForeignKey("region.id"))
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP)
