from sqlalchemy import BigInteger, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from typing import TYPE_CHECKING, List, Optional
from datetime import datetime

if TYPE_CHECKING:
    from app.models.repository import Repository
    from app.models.github_total_data import GithubTotalData
    from app.models.github_score import GithubScore

class GithubAccount(Base):
    __tablename__ = "github_account"

    github_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True) # 깃허브에서 제공하는 고유 id
    github_login: Mapped[str] = mapped_column(String(255))
    github_token: Mapped[Optional[str]] = mapped_column(String(255))
    last_synced_at: Mapped[Optional[datetime]] = mapped_column(DateTime, default=datetime.now())

    # 관계 설정: github_account 테이블과 repository 테이블 간의 1:N 관계
    repositories: Mapped[List["Repository"]] = relationship("Repository",
                                back_populates="github_account",
                                cascade="all, delete-orphan")
    
    # 관계 설정: github_account 테이블과 github_total_data 테이블 간의 1:N 관계
    github_total_data : Mapped[List["GithubTotalData"]] = relationship("GithubTotalData",
                                     back_populates="github_account")
    
    # 관계 설정: github_account 테이블과 github_score 테이블 간의 1:N 관계
    github_score : Mapped[List["GithubScore"]] = relationship("GithubScore",
                                back_populates="github_account")