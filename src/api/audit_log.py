from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, List
from src.core.db import get_db as get_session
from src.service import audit_log_service
from src.schemas.audit_log import AuditLogRead

router = APIRouter(prefix="/audit-log", tags=["Audit Log"])


@router.get("/", response_model=List[AuditLogRead])
async def get_audit_logs(
    user_type: Optional[str] = Query(None, description="Filter by user_type"),
    user_id: Optional[int] = Query(None, description="Filter by user_id"),
    entity: Optional[str] = Query(None, description="Filter by entity"),
    entity_id: Optional[int] = Query(None, description="Filter by entity_id"),
    session: AsyncSession = Depends(get_session),
):
    return await audit_log_service.get_logs(
        session=session,
        user_type=user_type,
        user_id=user_id,
        entity=entity,
        entity_id=entity_id
    )
