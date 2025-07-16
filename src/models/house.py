from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP, func, Double
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship
from src.core.db import Base

class House(Base):
    __tablename__ = "house"
    id = Column(Integer, primary_key=True)
    unique_code = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    street_id = Column(Integer, ForeignKey("street.id"))
    house_number = Column(Text)
    latitude = Column(Double)
    longitude = Column(Double)
    created_by = Column(Integer, ForeignKey("employee.id"))
    created_at = Column(TIMESTAMP, server_default=func.now())

    residents = relationship("Resident", back_populates="house")
