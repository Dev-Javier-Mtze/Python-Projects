from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Hello"
    debug: bool = False
    http_url: str = "Hello world"
    error_http_url: str = "Magic"

    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).resolve().parent.parent.parent / ".env"),
        env_file_encoding="utf-8",
    )


settings = Settings()
print(settings.dict())
print(Path(__file__).resolve().parent.parent.parent / ".env")
