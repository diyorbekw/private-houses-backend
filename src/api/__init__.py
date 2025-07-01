from fastapi import APIRouter
from .study_direction import study_direction_router

api_router = APIRouter(
    prefix="/api"
)

api_router.include_router(study_direction_router)


