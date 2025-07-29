from sqlalchemy import Column, BigInteger, Integer, String, DateTime, Text, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from db import Base

class Repository(Base):
    __tablename__ = "repository"

    repo_id = Column(BigInteger, primary_key=True, index=True) # 깃허브에서 제공하는 고유 id
    github_id = Column(BigInteger, nullable=False) # FK
    owner_name = Column(String(255), nullable=False)
    repo_name = Column(String(255), nullable=False)
    default_branch = Column(String(255), nullable=False)
    score = Column(Integer, nullable=False)
    watcher = Column(Integer, nullable=False)
    star = Column(Integer, nullable=False)
    fork = Column(Integer, nullable=False)
    commit_count = Column(Integer, nullable=False)
    commit_line = Column(Integer, nullable=False)
    commit_del = Column(Integer, nullable=False)
    commit_add = Column(Integer, nullable=False)
    unmerged_commit_count = Column(Integer, nullable=False)
    unmerged_commit_line = Column(Integer, nullable=False)
    unmerged_commit_del = Column(Integer, nullable=False)
    unmerged_commit_add = Column(Integer, nullable=False)
    pr = Column(Integer, nullable=False)
    issue = Column(Integer, nullable=False)
    depedency = Column(Integer, nullable=False)
    description = Column(String(255), nullable=False)
    readme = Column(Text, nullable=False)
    license = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    pushed_at = Column(DateTime, nullable=False)
    language = Column(Text, nullable=False) # json 형태지만, 통계 등에 따로 사용하지 않아 문자열로 저장. 추후 변경 가능
    contributor = Column(Integer, nullable=False)
    is_private = Column(Boolean, nullable=False)
    
    # 관계 설정: github_account 테이블과 repository 테이블 간의 1:N 관계
    github_account_id = Column(Integer, ForeignKey("github_account.github_id"), nullable=False)
    github_account = relationship("GithubAccount", back_populates="repositories")

    # 관계 설정: repository 테이블과 commit 테이블 간의 1:N 관계
    commits = relationship("Commit", 
                           back_populates="repository",
                           cascade="all, delete-orphan")
    
    # 관계 설정: repository 테이블과 pull_request 테이블 간의 1:N 관계
    pull_requests = relationship("PullRequest", 
                                back_populates="repository",
                                cascade="all, delete-orphan")

    # 관계 설정: repository 테이블과 issue 테이블 간의 1:N 관계
    issues = relationship("Issue", 
                         back_populates="repository",
                         cascade="all, delete-orphan")
    
    # 관계 설정: repository 테이블과 star 테이블 간의 1:N 관계
    stars = relationship("Star", 
                         back_populates="repository",
                         cascade="all, delete-orphan")
    
    # 관계 설정: repository 테이블과 fork 테이블 간의 1:N 관계
    forks = relationship("Fork", 
                         back_populates="repository",
                         cascade="all, delete-orphan")

    # 복합 유니크 키 설정
    __table_args__ = (
        UniqueConstraint("github_id", "owner_name", "repo_name", name="uq_repo_identifier"),
    )

    @property
    def repo_full_name(self):
        return f"{self.owner_name}/{self.repo_name}"