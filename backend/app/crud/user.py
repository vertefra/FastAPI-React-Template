from os import stat

import bcrypt
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.session import Session

from app import crud
from app.crud.basic import CRUDBasic
from app.models import User
from app.pydantic_models import SignupUser, UpdateUser
from app.pydantic_models.user import CreatedUser, LoginUser


class UserCRUD(CRUDBasic[User, SignupUser, UpdateUser]):
    async def get_by_username(self, db: Session, username: str) -> User:
        return db.query(User).filter(User.username == username).one_or_none()

    async def get_by_email(self, db: Session, email: str) -> User:
        return db.query(User).filter(User.email == email).one_or_none()

    async def create(self, db: Session, user_in: SignupUser) -> CreatedUser:

        user_by_username = await crud.user.get_by_username(db, username=user_in.username)

        if user_by_username:
            raise HTTPException(
                status_code=400, detail="Email or Username already in use"
            )

        user_by_email = await crud.user.get_by_email(db, email=user_in.email)

        if user_by_email:
            raise HTTPException(
                status_code=400, detail="Email or Username already in use"
            )

        hashed_password = bcrypt.hashpw(
            user_in.password.encode("UTF-8"), bcrypt.gensalt()
        )

        user_db = User(
            name=user_in.name,
            email=user_in.email,
            username=user_in.username,
            hashed_password=hashed_password.decode("UTF-8"),
        )

        db.add(user_db)
        db.commit()
        db.refresh(user_db)

        created_user = CreatedUser(
            id=user_db.id,
            username=user_db.username,
            email=user_db.email,
            password=user_in.password,
            created_at=user_db.created_at,
        )

        return created_user

    async def get(self, db: Session, *, user_in: LoginUser) -> User:

        user_db = crud.user.get_by_username(db, username=user_in.username)

        if not user_db:
            raise HTTPException(
                status_code=401, detail="Incorrect Username or Password"
            )

        valid_password = bcrypt.checkpw(
            user_in.password.encode("UTF-8"),
            hashed_password=user_db.hashed_password.encode("UTF-8"),
        )

        if not valid_password:
            raise HTTPException(
                status_code=401, detail="Incorrect Username or Password"
            )

        return user_db


user = UserCRUD(User)
