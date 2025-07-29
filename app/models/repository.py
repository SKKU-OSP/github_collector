from sqlalchemy import BigInteger, Integer, String, DateTime, Text, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from datetime import datetime
from typing import TYPE_CHECKING, Optional, List

if TYPE_CHECKING:
    from app.models.github_account import GithubAccount
    from app.models.commit import Commit
    from app.models.pull_request import PullRequest
    from app.models.issue import Issue
    from app.models.star import Star
    from app.models.fork import Fork

class Repository(Base):
    __tablename__ = "repository"

    repo_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True) # 깃허브에서 제공하는 고유 id
    github_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("github_account.github_id"))
    owner_name: Mapped[str] = mapped_column(String(255))
    repo_name: Mapped[str] = mapped_column(String(255))
    default_branch: Mapped[str] = mapped_column(String(255))
    score: Mapped[int] = mapped_column(Integer, default=0)
    watcher: Mapped[int] = mapped_column(Integer, default=0)
    star: Mapped[int] = mapped_column(Integer, default=0)
    fork: Mapped[int] = mapped_column(Integer, default=0)
    commit_count: Mapped[int] = mapped_column(Integer, default=0)
    commit_line: Mapped[int] = mapped_column(Integer, default=0)
    commit_del: Mapped[int] = mapped_column(Integer, default=0)
    commit_add: Mapped[int] = mapped_column(Integer, default=0)
    unmerged_commit_count: Mapped[int] = mapped_column(Integer, default=0)
    unmerged_commit_line: Mapped[int] = mapped_column(Integer, default=0)
    unmerged_commit_del: Mapped[int] = mapped_column(Integer, default=0)
    unmerged_commit_add: Mapped[int] = mapped_column(Integer, default=0)
    pr: Mapped[int] = mapped_column(Integer, default=0)
    issue: Mapped[int] = mapped_column(Integer, default=0)
    depedency: Mapped[int] = mapped_column(Integer, default=0)
    description: Mapped[Optional[str]] = mapped_column(String(255))
    readme: Mapped[Optional[str]] = mapped_column(Text)
    license: Mapped[Optional[str]] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    pushed_at: Mapped[datetime] = mapped_column(DateTime)
    language: Mapped[Optional[str]] = mapped_column(Text) # json 형태지만, 통계 등에 따로 사용하지 않아 문자열로 저장. 추후 변경 가능
    contributor: Mapped[int] = mapped_column(Integer, default=0)
    is_private: Mapped[bool] = mapped_column(Boolean, default=False)
    
    # 관계 설정: github_account 테이블과 repository 테이블 간의 1:N 관계
    github_account: Mapped["GithubAccount"] = relationship("GithubAccount", back_populates="repositories")

    # 관계 설정: repository 테이블과 commit 테이블 간의 1:N 관계
    commits: Mapped[List["Commit"]] = relationship("Commit", 
                           back_populates="repository",
                           cascade="all, delete-orphan")
    
    # 관계 설정: repository 테이블과 pull_request 테이블 간의 1:N 관계
    pull_requests: Mapped[List["PullRequest"]] = relationship("PullRequest", 
                                back_populates="repository",
                                cascade="all, delete-orphan")

    # 관계 설정: repository 테이블과 issue 테이블 간의 1:N 관계
    issues: Mapped[List["Issue"]] = relationship("Issue", 
                         back_populates="repository",
                         cascade="all, delete-orphan")
    
    # 관계 설정: repository 테이블과 star 테이블 간의 1:N 관계
    stars: Mapped[List["Star"]] = relationship("Star", 
                         back_populates="repository",
                         cascade="all, delete-orphan")
    
    # 관계 설정: repository 테이블과 fork 테이블 간의 1:N 관계
    forks: Mapped[List["Fork"]] = relationship("Fork", 
                         back_populates="repository",
                         cascade="all, delete-orphan")

    # 복합 유니크 키 설정
    __table_args__ = (
        UniqueConstraint("github_id", "owner_name", "repo_name", name="uq_repo_identifier"),
    )

    @property
    def repo_full_name(self):
        return f"{self.owner_name}/{self.repo_name}"