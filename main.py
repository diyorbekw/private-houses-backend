from fastapi import FastAPI
from fastapi.security import HTTPBearer
from src.api import api_router
import uvicorn

app = FastAPI(
    title="Private Houses Backend API",
    description="API for managing private houses and residents",
    version="1.0.0",
    openapi_tags=[
        {"name": "Auth", "description": "Operations with authentication"},
        {"name": "Employees", "description": "Operations with employees"},
        {"name": "Residents", "description": "Operations with residents"},
        {"name": "Houses", "description": "Operations with houses"},
        {"name": "Territories", "description": "Operations with territories"},
        {"name": "Verification", "description": "Operations with verification codes"},
        {"name": "Audit Log", "description": "Operations with audit logs"},
    ]
)

security_scheme = HTTPBearer()

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True , port=8001)
