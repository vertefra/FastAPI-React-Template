from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.config import settings

engine = create_engine(settings.DB_CONNECTION_STRING)

LocalSession = sessionmaker(bind=engine, autocommit=False)


def get_db() -> Generator:
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
