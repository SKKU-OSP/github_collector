from sqlalchemy import Column, BigInteger, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from db import Base

class Fork(Base):
    __tablename__ = "fork"

    id = Column(BigInteger, primary_key=True, index=True) # auto increment
    repo_id = Column(BigInteger, nullable=False) # FK
    fork_user_id = Column(BigInteger, nullable=False)
    fork_date = Column(DateTime, nullable=False)

    # 관계 설정: repository 테이블과 fork 테이블 간의 1:N 관계
    repo_id = Column(BigInteger, ForeignKey("repository.repo_id"), nullable=False)
    repository = relationship("Repository", back_populates="forks")

    # 복합 유니크 키 설정
    __table_args__ = (
        UniqueConstraint("repo_id", "fork_user_id", name="uq_fork_identifier"),
    )