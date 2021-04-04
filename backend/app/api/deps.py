from os import SEEK_CUR

from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends, Header

from app.config import settings


def is_portal(x_api_key: str = Header(None)) -> bool:
    if x_api_key == settings.PORTAL_KEY:
        return True
    raise HTTPException(status_code=403, detail="Not Authorized")
