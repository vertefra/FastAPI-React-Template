from typing import Generic, List, Optional, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import Base

Model = TypeVar("Model", bound=Base)
CreateSchema = TypeVar("CreateSchema", bound=BaseModel)
UpdateSchema = TypeVar("UpdateSchema", bound=BaseModel)


class CRUDBasic(Generic[Model, CreateSchema, UpdateSchema]):
    def __init__(self, model: Type[Model]):
        self.model = model

    async def get_multi(
        self,
        db: Session,
        *,
        get_deactivated: bool = False,
        skip: int = 0,
        limit: int = 100,
    ) -> List[Optional[Model]]:
        if get_deactivated:
            return db.query(self.model).offset(offset=skip).limit(limit=limit).all()

        return db.query(self.model).filter(self.model.is_active).all()

    async def get(
        self, db: Session, *, id: int, get_deactivated: bool = False
    ) -> Optional[Model]:
        if get_deactivated:
            return db.query(self.model).filter(self.model.id == id).one_or_none()

        return (
            db.query(self.model)
            .filter(self.model.id == id)
            .filter(self.model.is_active)
            .one_or_none()
        )

    async def create(self, db: Session, *, obj_in: CreateSchema) -> Model:
        obj_db = self.model(**obj_in.dict())
        db.add(obj_db)
        db.commit()
        db.refresh(obj_db)
        return obj_db

    async def update(
        self, db: Session, *, id: int, obj_db: Model, obj_update: UpdateSchema
    ) -> Model:

        obj_db = db.query(self.model).filter(self.model.id == id).one()
        obj_update_dict = obj_update.dict()
        for field in obj_update_dict:
            if obj_update_dict[field]:
                setattr(obj_db, field, obj_update_dict[field])
        db.add(obj_db)
        db.commit()
        db.refresh(obj_db)

        return obj_db
