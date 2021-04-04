import uvicorn
from fastapi import FastAPI

from app.api.router import router
from app.config import settings
from app.prestart import init_db

init_db()

app = FastAPI()


app.include_router(router, prefix=settings.URL_PREFIX)


if __name__ == "__main__":
    uvicorn.run(
        "main:app", port=int(settings.PORT), host=settings.HOST, reload=settings.RELOAD
    )
