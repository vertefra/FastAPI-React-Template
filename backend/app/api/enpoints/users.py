from typing import Any, List

from fastapi import APIRouter, Depends
from fastapi.param_functions import Query
from sqlalchemy.orm.session import Session

from app import crud
from app.api.deps import is_portal
from app.database import get_db
from app.pydantic_models import SignupUser, User, UserGET
from app.pydantic_models.user import LoginUser

router = APIRouter()


@router.get("/", response_model=List[UserGET], response_model_exclude_none=True)
async def get_users(
    db: Session = Depends(get_db),
    portal: bool = Depends(is_portal),
    *,
    get_deactivated: bool = Query(False),
    skip: int = Query(0),
    limit: int = Query(100),
) -> Any:
    """
    Gets all the users
    """

    return await crud.user.get_multi(
        db, skip=skip, limit=limit, get_deactivated=get_deactivated
    )


@router.post("/signup", response_model=User, response_model_exclude_none=True)
async def signup_user(
    db: Session = Depends(get_db),
    portal: bool = Depends(is_portal),
    *,
    user_signup: SignupUser,
) -> Any:

    return await crud.user.create(db, user_in=user_signup)


@router.post("/login", response_model=UserGET, response_model_exclude_none=True)
async def login_user(
    db: Session = Depends(get_db),
    portal: bool = Depends(is_portal),
    *,
    user_login: LoginUser,
) -> Any:

    return await crud.user.get(db, user_in=user_login)
