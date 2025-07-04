from fastapi import APIRouter
from .study_direction import study_direction_router
from .study_language import study_language_router
from .study_form import study_form_router
from .auth import auth_router


api_router = APIRouter(
    prefix="/api"
)

api_router.include_router(auth_router)
api_router.include_router(study_language_router)
api_router.include_router(study_direction_router)
api_router.include_router(study_form_router)

