from fastapi import FastAPI

from app.core.config import APP_NAME, APP_VERSION

from app.database.connection import engine
from app.database.base import Base

from app.models import User, History

from app.routers.auth_router import router as auth_router
from app.routers.calculator_router import router as calculator_router
from app.routers.history_router import router as history_router
from app.routers.statistics_router import router as statistics_router
from app.routers.health_router import router as health_router
from app.routers.export_router import router as export_router
from app.routers.profile_router import router as profile_router

from app.utils.logger import logger
from app.middleware import LoggingMiddleware

from app.core.exceptions import (
    APIException,
    api_exception_handler
)

logger.info("Application Started Successfully")

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Enterprise Smart Calculator API"
)

app.add_exception_handler(
    APIException,
    api_exception_handler
)

app.add_middleware(LoggingMiddleware)

app.include_router(auth_router)
app.include_router(calculator_router)
app.include_router(history_router)
app.include_router(statistics_router)
app.include_router(health_router)
app.include_router(export_router)
app.include_router(profile_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Smart Calculator Pro API",
        "version": APP_VERSION
    }