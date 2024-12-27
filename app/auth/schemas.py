from pydantic import BaseModel, EmailStr

class SignupRequest(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str
    
class LoginRequest(BaseModel):
    email: EmailStr
    password: str
