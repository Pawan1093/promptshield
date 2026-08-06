from fastapi import APIRouter
from app.configuration.config import settings

router = APIRouter()

@router.get("/")
def home():
      return {
        "project": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "debug": settings.DEBUG,
        "status": "Running Successfully"
    }




