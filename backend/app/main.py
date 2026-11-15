from fastapi import FastAPI

app = FastAPI(
    title="AI 3D Environment Platform",
    description="Intelligent 3D Environment Reconstruction and Generation API",
    version="1.0.0",
)


@app.get("/api/v1/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "message": "Backend is running successfully",
    }