from fastapi import APIRouter, Depends
from src.schemas.auth import LoginRequest, RegisterRequest
from src.service.auth import AuthService
from src.core.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


async def get_auth_service(session: AsyncSession = Depends(get_db)) -> AuthService:
    return AuthService(session)


@auth_router.post("/login")
async def login(
    login_data: LoginRequest,
    auth_service: AuthService = Depends(get_auth_service),
):
    return await auth_service.login(login_data)

@auth_router.post("/register")
async def register(
    request: RegisterRequest, 
    auth_service: AuthService = Depends(get_auth_service)
):
    return await auth_service.register(request)