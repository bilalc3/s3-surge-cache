from fastapi import FastAPI
from app.api.routers import router as api_router  # Import the API router
from app.core.config import settings  # Import the configuration settings

app = FastAPI(title=settings.app_name, version="1.0.0", description="AWS Surge Cache System")


app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.app_name}!"}
