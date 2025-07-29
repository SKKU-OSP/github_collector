from sqlalchemy import Column, BigInteger, Integer, String, DateTime, Text, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from db import Base

class Issue(Base):
    __tablename__ = "issue"

    issue_id = Column(BigInteger, primary_key=True, index=True) # 깃허브에서 제공하는 고유 id
    repo_id = Column(BigInteger, nullable=False) # FK
    issue_number = Column(Integer, nullable=False)
    issue_title = Column(String(255), nullable=False)
    issue_body = Column(Text, nullable=False)
    issue_date = Column(DateTime, nullable=False)

    # 관계 설정: repository 테이블과 issue 테이블 간의 1:N 관계
    repo_id = Column(BigInteger, ForeignKey("repository.repo_id"), nullable=False)
    repository = relationship("Repository", back_populates="issues")

    # 복합 유니크 키 설정
    __table_args__ = (
        UniqueConstraint("repo_id", "issue_number", name="uq_issue_identifier"),
    )