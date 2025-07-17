from src.models import AuditLog
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

class AuditLogger:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def log(
        self,
        user_type: str,
        user_id: int,
        action: str,
        entity: str,
        entity_id: int,
        old_value: dict | None,
        new_value: dict | None
    ):
        log = AuditLog(
            user_type=user_type,
            user_id=user_id,
            action=action,
            entity=entity,
            entity_id=entity_id,
            old_value=old_value,
            new_value=new_value,
            timestamp=datetime.utcnow()
        )
        self.session.add(log)
        await self.session.flush()