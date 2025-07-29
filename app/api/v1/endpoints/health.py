from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.api.deps import get_db

router = APIRouter()

@router.get("/ping")
def ping():
    """API 상태 확인"""
    return {"message": "pong"}

@router.get("/ping-db")
def ping_db(db: Session = Depends(get_db)):
    """데이터베이스 연결 확인"""
    try:
        result = db.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        return {"status": "error", "message": str(e)}