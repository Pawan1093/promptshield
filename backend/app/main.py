from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "project":"promptshield",
        "status":"running application successfully"
    }