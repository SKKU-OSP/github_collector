from sqlalchemy import BigInteger, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.repository import Repository

class Star(Base):
    __tablename__ = "star"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True) # auto increment
    repo_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("repository.repo_id"))
    star_user_id: Mapped[int] = mapped_column(BigInteger)
    star_date: Mapped[datetime] = mapped_column(DateTime)

    # 관계 설정: repository 테이블과 star 테이블 간의 1:N 관계
    repository: Mapped["Repository"] = relationship("Repository", back_populates="stars")

    # 복합 유니크 키 설정
    __table_args__ = (
        UniqueConstraint("repo_id", "star_user_id", name="uq_star_identifier"),
    )