from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime


class AuditLogCreate(BaseModel):
    user_type: str 
    user_id: int
    action: str
    entity: str
    entity_id: int
    old_value: Optional[dict]
    new_value: Optional[dict]


class AuditLogResponse(BaseModel):
    id: int
    user_type: str
    user_id: int
    action: str
    entity: str
    entity_id: int
    old_value: Optional[Any]
    new_value: Optional[Any]
    timestamp: datetime

    class Config:
        from_attributes = True

class AuditLogRead(BaseModel):
    id: int
    user_type: str
    user_id: int
    action: str
    entity: str
    entity_id: int
    old_value: Optional[dict]
    new_value: Optional[dict]
    timestamp: datetime

    class Config:
        from_attributes = True
