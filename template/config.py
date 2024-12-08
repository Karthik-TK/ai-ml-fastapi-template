import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    FASTAPI_CONFIG: str = os.getenv("FASTAPI_CONFIG")
    DOMAIN_WHITELISTED: list = os.getenv("DOMAIN_WHITELISTED")
    ALLOW_CREDENTIALS: bool = os.getenv("ALLOW_CREDENTIALS")
    ALLOW_METHODS: list = os.getenv("ALLOW_METHODS")
    ALLOW_HEADERS: list = os.getenv("ALLOW_HEADERS")

    # Add more settings here


settings = Settings()
