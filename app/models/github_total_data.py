from sqlalchemy import BigInteger, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.github_account import GithubAccount

class GithubTotalData(Base):
    __tablename__ = "github_total_data"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True) # auto increment
    github_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("github_account.github_id"))
    year: Mapped[int] = mapped_column(Integer)
    commit_line: Mapped[int] = mapped_column(Integer, default=0)
    commit_count: Mapped[int] = mapped_column(Integer, default=0)
    pr_count: Mapped[int] = mapped_column(Integer, default=0)
    issue_count: Mapped[int] = mapped_column(Integer, default=0)
    star_count: Mapped[int] = mapped_column(Integer, default=0)
    fork_count: Mapped[int] = mapped_column(Integer, default=0)
    score: Mapped[int] = mapped_column(Integer, default=0)

    # 관계 설정: github_account 테이블과 github_total_data 테이블 간의 1:N 관계
    github_account: Mapped["GithubAccount"] = relationship("GithubAccount", back_populates="github_total_data")

    # 복합 유니크 키 설정
    __table_args__ = (
        UniqueConstraint("github_id", "year", name="uq_github_id_year_data"),
    )