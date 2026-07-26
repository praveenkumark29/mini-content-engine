from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_ENV: str
    DATABASE_URL: str
    LOG_LEVEL: str

    llm_provider: str = "ollama"

    llm_provider: str = "ollama"

    image_provider: str = "mock"



    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()