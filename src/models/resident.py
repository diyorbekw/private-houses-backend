from sqlalchemy import Column, Integer, Text, Boolean, Date, TIMESTAMP, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from src.core.db import Base

class Resident(Base):
    __tablename__ = "resident"
    id = Column(Integer, primary_key=True)
    house_id = Column(Integer, ForeignKey("house.id", ondelete="CASCADE"))
    full_name = Column(Text)
    birth_date = Column(Date)
    gender = Column(Text)
    phone = Column(Text)
    passport_number = Column(Text)
    relationship_to_owner = Column(Text)
    is_owner = Column(Boolean, default=False)
    photo_url = Column(Text)
    created_at = Column(TIMESTAMP)

    __table_args__ = (
        CheckConstraint("gender IN ('male', 'female')"),
    )

    house = relationship("House", back_populates="residents")
