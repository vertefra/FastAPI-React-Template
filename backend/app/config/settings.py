import dotenv
from pydantic import BaseSettings

dotenv.load_dotenv()


class Settings(BaseSettings):

    APP_NAME: str

    ENV: str
    HOST: str
    PORT: str

    DB_PORT: str
    DB_HOST: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    PG_STRING: str = None
    DB_CONNECTION_STRING: str = None

    JWT_SECRET: str = None
    PORTAL_KEY: str = None

    DEBUG: bool = False
    RELOAD: bool = False

    URL_PREFIX = "/api/v1"

    def evaluate_environment(self) -> None:

        if self.ENV == "development":
            self.DEBUG = True
            self.RELOAD = True

        if self.ENV == "production":
            self.DEBUG = False
            self.RELOAD = False

    def set_db_connection_string(self) -> None:

        self.DB_CONNECTION_STRING = f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    def get_server_connection_string(self) -> str:
        """
        returns a string connection with server without specifing a database
        """

        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/"


settings = Settings()
settings.evaluate_environment()
settings.set_db_connection_string()
