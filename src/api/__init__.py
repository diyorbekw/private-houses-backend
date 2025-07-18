from fastapi import APIRouter, Depends
from src.utils.auth import require_role
from .resident import router as resident_router
from .house import router as house_router
from .territory import router as territory_router
from .employee import router as employee_router
from .auth import auth_router
from .verification import router as verification_router
from .audit_log import router as audit_log_router

api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(employee_router)
api_router.include_router(resident_router)
api_router.include_router(house_router)
api_router.include_router(territory_router)
api_router.include_router(verification_router)
api_router.include_router(audit_log_router, include_in_schema=False)