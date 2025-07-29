import time
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import OperationalError

from app.core import settings, engine, Base
from app.api.v1 import api_router

# 모든 모델을 import (Base.metadata에 등록하기 위해)
from app.models import (
    github_account,
    github_total_data,
    github_score,
    repository,
    commit,
    pull_request,
    issue,
    star,
    fork
)

def wait_for_db(retries: int = 30) -> None:
    """데이터베이스 연결 대기"""
    while retries > 0:
        try:
            conn = engine.connect()
            conn.close()
            print("Database is ready!")
            break
        except OperationalError:
            retries -= 1
            print(f"Database not ready. Retrying... ({retries} left)")
            time.sleep(2)
    else:
        raise Exception("Could not connect to database")

# TODO: 추후 alembic 적용 시 삭제
def init_db() -> None:
    """데이터베이스 초기화"""
    wait_for_db()
    print(f"Registered tables: {list(Base.metadata.tables.keys())}")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

@asynccontextmanager
async def lifespan(app: FastAPI):
    """애플리케이션 생명주기 관리"""
    # Startup
    print("Starting up...")
    init_db()
    yield
    # Shutdown
    print("Shutting down...")
    engine.dispose()

# FastAPI 앱 생성
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS 미들웨어 설정
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# API 라우터 등록
app.include_router(api_router, prefix=settings.API_V1_PREFIX)

# 루트 엔드포인트만 남김
@app.get("/", tags=["root"])
async def root():
    """API 정보 반환"""
    return {
        "message": "GitHub Collector API",
        "version": settings.VERSION,
        "docs": "/docs",
        "api": settings.API_V1_PREFIX
    }