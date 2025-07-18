from src.schemas.auth import LoginRequest, RegisterRequest
from src.models.admin_user import AdminUser
from src.utils.auth import hash_password, verify_password
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from datetime import datetime
from src.utils.auth import create_access_token, create_refresh_token


class AuthService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def login(self, request: LoginRequest):
        result = await self.session.execute(select(AdminUser).where(AdminUser.username == request.username))
        user = result.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        if not verify_password(request.password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": {
                "id": user.id,
                "username": user.username,
                "full_name": user.full_name,
                "role": user.role
            }
        }

    async def register(self, request: RegisterRequest):
        result = await self.session.execute(select(AdminUser).where(AdminUser.username == request.username))
        existing_user = result.scalar_one_or_none()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")
        
        new_user = AdminUser(
            username=request.username, 
            password_hash=hash_password(request.password), 
            full_name=request.full_name, 
            role=request.role,
            created_at=datetime.now()
        )
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return new_user