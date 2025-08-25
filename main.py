from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import os

app = FastAPI(
    title="Mon App FastAPI Simple",
    description="API simple pour déploiement CI/CD",
    version="1.0.0"
)

class MessageResponse(BaseModel):
    message: str
    version: str
    timestamp: str
    environment: str

class HealthResponse(BaseModel):
    status: str
    timestamp: str

@app.get("/", response_model=MessageResponse)
async def read_root():
    return MessageResponse(
        message="Hello World from FastAPI!",
        version="1.0.0",
        timestamp=datetime.now().isoformat(),
        environment=os.getenv("ENVIRONMENT", "development")
    )

@app.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="OK",
        timestamp=datetime.now().isoformat()
    )

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
