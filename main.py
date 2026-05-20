from fastapi import FastAPI

from config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.APP_VERSION,
)
