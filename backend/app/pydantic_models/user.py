from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseUser(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None
    hashed_password: Optional[str] = None
    email: Optional[str] = None
    is_admin: Optional[bool] = False
    is_active: Optional[bool] = True
    is_verified: Optional[bool] = False


class SignupUser(BaseUser):
    name: str
    username: str
    email: str
    is_admin: Optional[bool] = False
    password: str


class LoginUser(BaseUser):
    email: str
    password: str


class CreatedUser(BaseUser):
    id: int
    username: str
    email: str
    password: str
    created_at: datetime

    class Config:
        orm_mode = True


class UpdateUser(BaseUser):
    name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    is_admin: Optional[bool] = False
    password: Optional[str] = None
    is_active: Optional[bool] = True
    is_verified: Optional[bool] = False


class UserDB(BaseUser):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class UserGET(BaseModel):
    id: int
    created_at: datetime
    username: str
    email: str

    class Config:
        orm_mode = True


class User(UserDB):
    pass
