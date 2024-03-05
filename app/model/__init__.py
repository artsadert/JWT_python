from pydantic import BaseModel, SecretStr, EmailStr, Field


class UserRegistration(BaseModel):
    user_name: str
    email: EmailStr
    password: str
