from fastapi import FastAPI
from app.api.v1.endpoints.health import router as health_router

app = FastAPI(
    title="AI 3D Environment Platform",
    description="Intelligent 3D Environment Reconstruction and Generation API",
    version="0.1.0",
)

app.include_router(
    health_router,
    prefix="/api/v1/health",
)


@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "application": "AI 3D Environment Platform",
    }