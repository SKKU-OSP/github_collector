from sqlalchemy import Column, BigInteger, Integer, String, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class PullRequest(Base):
    __tablename__ = "pull_request"

    pr_id = Column(BigInteger, primary_key=True, index=True) # 깃허브에서 제공하는 고유 id
    repo_id = Column(BigInteger, nullable=False) # FK
    pr_number = Column(Integer, nullable=False)
    pr_title = Column(String(255), nullable=False)
    pr_body = Column(Text, nullable=False)
    pr_date = Column(DateTime, nullable=False)
    merged = Column(Boolean, nullable=False)
    base_branch = Column(String(255), nullable=False)
    head_branch = Column(String(255), nullable=False)

    # 관계 설정: repository 테이블과 pull_request 테이블 간의 1:N 관계
    repo_id = Column(BigInteger, ForeignKey("repository.repo_id"), nullable=False)
    repository = relationship("Repository", back_populates="pull_requests")