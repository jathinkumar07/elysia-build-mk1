from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite+aiosqlite:///./test.db"
    secret_key: str = "change-me"

settings = Settings()
