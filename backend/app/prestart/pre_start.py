import sys
import time
from typing import Union

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from app.config import settings
from app.database import Base


def _db_up() -> Union[Engine, bool]:

    db_ready: bool = False
    attemp: int = 1
    max_attemps: int = 3
    retry_time: int = 2
    print("Connecting with database...")
    while not db_ready or attemp <= max_attemps:

        conn_engine: Engine = None

        try:
            conn_engine = create_engine(
                settings.DB_CONNECTION_STRING,
            )

        except Exception as err:
            print(err)
            print("Database still offline")
            print(f"Attempt {attemp}")
            time.sleep(retry_time)
            attemp += 1

        return conn_engine

    return False


def init_db() -> None:
    engine = _db_up()

    if not engine:
        sys.exit("Could not retry databse connection")
    else:
        print("Creating tables...")
        Base.metadata.create_all(engine)
