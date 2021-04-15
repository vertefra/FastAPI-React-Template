import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import router
from app.config import settings
from app.prestart import init_db

init_db()

origins =  ['http://localhost:9000', 'http://0.0.0.0']

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(router, prefix=settings.URL_PREFIX)


if __name__ == "__main__":
    uvicorn.run(
        "main:app", port=int(settings.PORT), host=settings.HOST, reload=settings.RELOAD
    )
