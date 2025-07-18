from passlib.context import CryptContext
from src.core.config import settings
import jwt
from fastapi import HTTPException, Depends, Header, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.admin_user import AdminUser
from src.core.db import get_db
from typing import Optional, Callable

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Create a security scheme for Swagger documentation
security = HTTPBearer()


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)

def create_access_token(user_id: int) -> str:
    return jwt.encode({"sub": user_id}, settings.access_secret_key, algorithm=settings.algorithm)


def create_refresh_token(user_id: int) -> str:
    return jwt.encode({"sub": user_id}, settings.access_secret_key, algorithm=settings.algorithm)


async def get_current_user(token: str, session: AsyncSession) -> AdminUser:
    try:
        payload = jwt.decode(token, settings.access_secret_key, algorithms=[settings.algorithm])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = await session.execute(select(AdminUser).where(AdminUser.id == user_id))
        return user.scalar_one_or_none()
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    
    
async def get_current_user_by_role(token: str, role: str, session: AsyncSession) -> AdminUser:
    user = await get_current_user(token, session)
    if user.role != role:
        raise HTTPException(status_code=403, detail="Forbidden")
    return user


async def get_current_user_dependency(
    authorization: Optional[str] = Header(None),
    session: AsyncSession = Depends(get_db)
) -> AdminUser:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")
    
    token = authorization.replace("Bearer ", "")
    return await get_current_user(token, session)


def require_role(role: str) -> Callable:
    async def role_dependency(
        credentials: HTTPAuthorizationCredentials = Security(security),
        session: AsyncSession = Depends(get_db)
    ) -> AdminUser:
        token = credentials.credentials
        return await get_current_user_by_role(token, role, session)
    
    return role_dependency