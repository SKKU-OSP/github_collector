from sqlalchemy import BigInteger, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from datetime import datetime
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from app.models.repository import Repository

class Commit(Base):
    __tablename__ = "commit"

    sha: Mapped[str] = mapped_column(String(40), primary_key=True, index=True) # 40자 고정길이 해쉬값
    repo_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("repository.repo_id"))
    addiction: Mapped[int] = mapped_column(Integer)
    deletion: Mapped[int] = mapped_column(Integer)
    author_date: Mapped[datetime] = mapped_column(DateTime) # 커밋 작성자 시간
    committer_date: Mapped[datetime] = mapped_column(DateTime) # 푸시 시간
    message: Mapped[Optional[str]] = mapped_column(Text)
    branch: Mapped[str] = mapped_column(String(255))

    # 관계 설정: repository 테이블과 commit 테이블 간의 1:N 관계
    repository: Mapped["Repository"] = relationship("Repository", back_populates="commits")