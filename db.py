import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_DB = os.getenv("MYSQL_DB")

# MySQL 접속 URL 구성
DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

# SQLAlchemy 엔진 생성
engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)

# 세션 클래스 생성
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Base 클래스 (모든 모델이 상속받음)
Base = declarative_base()

# 의존성 주입용 함수 (FastAPI Depends에 사용)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
