from sqlalchemy import Column, Integer, Text, TIMESTAMP, CheckConstraint
from src.core.db import Base

class AdminUser(Base):
    __tablename__ = "admin_user"
    id = Column(Integer, primary_key=True)
    username = Column(Text, unique=True)
    password_hash = Column(Text)
    full_name = Column(Text)
    role = Column(Text)
    created_at = Column(TIMESTAMP)

    __table_args__ = (
        CheckConstraint("role IN ('admin', 'supervisor')"),
    )
