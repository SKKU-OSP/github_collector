from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Repository(Base):
    __tablename__ = "repository"

    id = Column(Integer, primary_key=True, index=True)
    github_id = Column(Integer, nullable=False)
    owner_name = Column(String(255), nullable=False)
    repo_name = Column(String(255), nullable=False)
    repo_full_name = Column(String(255), nullable=False)
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
