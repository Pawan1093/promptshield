from fastapi import FastAPI
from app.configuration.config import settings

app = FastAPI()

@app.get("/")
def home():
    return {
        "project":settings.APP_NAME,
        "version":settings.APP_VERSION,
        "debug":settings.DEBUG,
        "status":"running application successfully"
    }