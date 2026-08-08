import logging

from fastapi import FastAPI

from app.configuration.logging_config import setup_logging
from app.routers.home import router as home_router


setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(home_router)

logger.info("PromptShield application started")