from datetime import datetime

from sqlalchemy import Column, Text
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Integer

from app.database.Base import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, index=True, autoincrement=True, primary_key=True)
    username = Column(Text, nullable=False, unique=True)
    hashed_password = Column(Text, nullable=False)
    email = Column(Text, nullable=False, unique=True)
    is_admin = Column(Boolean, nullable=False, default=False)
    is_active = Column(Boolean, nullable=False, default=True)
    is_verified = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.now())
