from sqlalchemy import BigInteger, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.github_account import GithubAccount

class GithubScore(Base):
    __tablename__ = "github_score"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True) # auto increment
    github_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("github_account.github_id"))
    year: Mapped[int] = mapped_column(Integer)
    best_repo_name: Mapped[str] = mapped_column(String(255))
    activity_level_score: Mapped[int] = mapped_column(Integer, default=0)
    activity_diversity_score: Mapped[int] = mapped_column(Integer, default=0)
    activity_influence_score: Mapped[int] = mapped_column(Integer, default=0)
    score: Mapped[int] = mapped_column(Integer, default=0)

    # 관계 설정: github_account 테이블과 github_score 테이블 간의 1:N 관계
    github_account: Mapped["GithubAccount"] = relationship("GithubAccount", back_populates="github_score")

    # 복합 유니크 키 설정
    __table_args__ = (
        UniqueConstraint("github_id", "year", name="uq_github_id_year_score"),
    )