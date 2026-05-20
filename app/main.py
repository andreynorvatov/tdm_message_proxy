import structlog
from fastapi import FastAPI

from app.api.grafana import router as grafana_router
from app.api.health import router as health_router
from app.api.tdm import router as tdm_router
from app.config import settings
from app.logging import setup_logging

setup_logging()
logger = structlog.get_logger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.APP_VERSION,
)

app.include_router(grafana_router)
app.include_router(health_router)
app.include_router(tdm_router)

logger.info(
    "Приложение запущено",
    project=settings.PROJECT_NAME,
    version=settings.APP_VERSION,
    log_level=settings.LOG_LEVEL,
)
