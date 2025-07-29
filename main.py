from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import SessionLocal, engine, Base

app = FastAPI()

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

# 데이터베이스 테이블 생성
# TODO: 추후 alembic 적용 시 삭제
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()