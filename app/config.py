from typing import Literal

from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    PROJECT_NAME: str = Field(..., description="Наименование проекта")
    APP_VERSION: str = Field(..., description="Версия приложения")

    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="INFO", description="Уровень логирования"
    )
    LOG_FILE_PATH: str = Field(
        default="logs/app.log", description="Путь к файлу логов"
    )
    LOG_FILE_MAX_BYTES: int = Field(
        default=10485760, description="Максимальный размер файла логов (байты)"
    )
    LOG_FILE_BACKUP_COUNT: int = Field(
        default=5, description="Количество ротированных файлов логов"
    )

    NT_BOT_TDM_ID: int = Field(..., description="ID бота в TDM")
    NT_BOT_TDM_CHAT_ID: int = Field(..., description="ID чата в TDM")

    NT_BOT_TDM_AUTH_TOKEN: str = Field(..., description="Токен аутентификации")
    TDM_API_URL: str = Field(..., description="TDM API URL")

    @computed_field
    def NT_BOT_TDM_FULL_CHAT_URL(self) -> str:
        return f"{self.TDM_API_URL}/{self.NT_BOT_TDM_ID}/{self.NT_BOT_TDM_CHAT_ID}"


settings = Settings()  # type: ignore[call-arg]
