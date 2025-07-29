from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.core.database import Base

class GithubScore(Base):
    __tablename__ = "github_score"

    id = Column(BigInteger, primary_key=True, index=True) # auto increment
    github_id = Column(BigInteger, ForeignKey("github_account.github_id"), nullable=False)
    year = Column(Integer, nullable=False)
    best_repo_name = Column(String(255), nullable=False)
    activity_level_score = Column(Integer, nullable=False)
    activity_diversity_score = Column(Integer, nullable=False)
    activity_influence_score = Column(Integer, nullable=False)
    score = Column(Integer, nullable=False)

    # 관계 설정: github_account 테이블과 github_score 테이블 간의 1:N 관계
    github_account = relationship("GithubAccount", back_populates="github_score")

    # 복합 유니크 키 설정
    __table_args__ = (
        UniqueConstraint("github_id", "year", name="uq_github_id_year_score"),
    )