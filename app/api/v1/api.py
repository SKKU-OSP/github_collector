from fastapi import APIRouter
from app.api.v1.endpoints import health

api_router = APIRouter()

# Health check 라우터
api_router.include_router(
    health.router,
    prefix="/health",
    tags=["health"]
)
