from sqlalchemy import Column, Integer, Text, TIMESTAMP, JSON, CheckConstraint
from src.core.db import Base

class AuditLog(Base):
    __tablename__ = "audit_log"
    id = Column(Integer, primary_key=True)
    user_type = Column(Text)
    user_id = Column(Integer)
    action = Column(Text)
    entity = Column(Text)
    entity_id = Column(Integer)
    old_value = Column(JSON)
    new_value = Column(JSON)
    timestamp = Column(TIMESTAMP)

    __table_args__ = (
        CheckConstraint("user_type IN ('admin', 'employee')"),
    )
