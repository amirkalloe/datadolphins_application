import os
from pydantic import BaseSettings
from app.core.defaults import Defaults


class Settings(BaseSettings):
    USERFILE_PATH: str = os.getenv("USERFILE_PATH", Defaults.USERFILE_PATH)


settings = Settings()
