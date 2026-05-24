from fastapi import FastAPI

from backend.api.routes_incidents import router as incidents_router
from backend.api.routes_ai import router as ai_router

app = FastAPI(
    title="RCA Copilot API",
    description="AI Incident Intelligence Backend",
    version="1.0.0"
)

app.include_router(incidents_router, prefix="/api")
app.include_router(ai_router, prefix="/api")


@app.get("/")
def root():
    return {
        "message": "RCA Copilot backend is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }