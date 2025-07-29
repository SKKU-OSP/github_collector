import time
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from db import SessionLocal, engine, Base
import models.github_account
import models.github_total_data
import models.github_score
import models.repository
import models.commit
import models.pull_request
import models.issue
import models.star
import models.fork


# 데이터베이스 연결 대기
def wait_for_db():
    retries = 30
    while retries > 0:
        try:
            # 연결 테스트
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

# 데이터베이스 테이블 생성
def init_db():
    wait_for_db()  # DB 연결 대기
    print(f"Registered tables: {list(Base.metadata.tables.keys())}")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully")

# Lifespan 컨텍스트 매니저
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting up...")
    init_db()
    yield
    # Shutdown
    print("Shutting down...")

# FastAPI 앱 생성 시 lifespan 전달
app = FastAPI(lifespan=lifespan)

# 데이터베이스 세션 생성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 데이터베이스 연결 확인
@app.get("/ping-db")
def ping_db(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"status": "ok"}