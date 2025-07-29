from sqlalchemy import Column, BigInteger, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.core.database import Base

class Star(Base):
    __tablename__ = "star"

    id = Column(BigInteger, primary_key=True, index=True) # auto increment
    repo_id = Column(BigInteger, ForeignKey("repository.repo_id"), nullable=False)
    star_user_id = Column(BigInteger, nullable=False)
    star_date = Column(DateTime, nullable=False)

    # 관계 설정: repository 테이블과 star 테이블 간의 1:N 관계
    repository = relationship("Repository", back_populates="stars")

    # 복합 유니크 키 설정
    __table_args__ = (
        UniqueConstraint("repo_id", "star_user_id", name="uq_star_identifier"),
    )