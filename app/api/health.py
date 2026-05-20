from fastapi import APIRouter

from app.config import settings
from app.models.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Проверка работоспособности приложения."""
    return HealthResponse(
        status="ok",
        version=settings.APP_VERSION,
        project=settings.PROJECT_NAME,
    )
