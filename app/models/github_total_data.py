from sqlalchemy import Column, BigInteger, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.core.database import Base

class GithubTotalData(Base):
    __tablename__ = "github_total_data"

    id = Column(BigInteger, primary_key=True, index=True) # auto increment
    github_id = Column(BigInteger, ForeignKey("github_account.github_id"), nullable=False)
    year = Column(Integer, nullable=False)
    commit_line = Column(Integer, nullable=False)
    commit_count = Column(Integer, nullable=False)
    pr_count = Column(Integer, nullable=False)
    issue_count = Column(Integer, nullable=False)
    star_count = Column(Integer, nullable=False)
    fork_count = Column(Integer, nullable=False)
    score = Column(Integer, nullable=False)

    # 관계 설정: github_account 테이블과 github_total_data 테이블 간의 1:N 관계
    github_account = relationship("GithubAccount", back_populates="github_total_data")

    # 복합 유니크 키 설정
    __table_args__ = (
        UniqueConstraint("github_id", "year", name="uq_github_id_year_data"),
    )