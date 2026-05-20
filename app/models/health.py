from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Модель ответа health-эндпоинта."""

    status: str = Field(..., description="Статус работоспособности приложения")
    version: str = Field(..., description="Версия приложения")
    project: str = Field(..., description="Название проекта")
