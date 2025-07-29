from sqlalchemy import BigInteger, Integer, String, DateTime, Text, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from datetime import datetime
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from app.models.repository import Repository

class PullRequest(Base):
    __tablename__ = "pull_request"

    pr_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True) # 깃허브에서 제공하는 고유 id
    repo_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("repository.repo_id"))
    pr_number: Mapped[int] = mapped_column(Integer)
    pr_title: Mapped[str] = mapped_column(String(255))
    pr_body: Mapped[Optional[str]] = mapped_column(Text)
    pr_date: Mapped[datetime] = mapped_column(DateTime)
    merged: Mapped[bool] = mapped_column(Boolean, default=False)
    base_branch: Mapped[str] = mapped_column(String(255))
    head_branch: Mapped[str] = mapped_column(String(255))

    # 관계 설정: repository 테이블과 pull_request 테이블 간의 1:N 관계
    repository: Mapped["Repository"] = relationship("Repository", back_populates="pull_requests")

    # 복합 유니크 키 설정
    __table_args__ = (
        UniqueConstraint("repo_id", "pr_number", name="uq_pr_identifier"),
    )