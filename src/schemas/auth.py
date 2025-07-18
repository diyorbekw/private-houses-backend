from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    
    
class RegisterRequest(BaseModel):
    username: str
    password: str
    full_name: str
    role: str
    
    
class RegisterResponse(BaseModel):
    id: int
    username: str