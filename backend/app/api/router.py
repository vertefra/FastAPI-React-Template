from fastapi import APIRouter

from app.api.endpoints import users

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["Users"])
