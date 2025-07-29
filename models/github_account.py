from sqlalchemy import Column, BigInteger, String, DateTime
from sqlalchemy.orm import relationship
from db import Base

class GithubAccount(Base):
    __tablename__ = "github_account"

    github_id = Column(BigInteger, primary_key=True, index=True) # 깃허브에서 제공하는 고유 id
    github_login = Column(String(255), nullable=False)
    github_token = Column(String(255), nullable=True)
    last_synced_at = Column(DateTime)

    # 관계 설정: github_account 테이블과 repository 테이블 간의 1:N 관계
    repositories = relationship("Repository",
                                back_populates="github_account",
                                cascade="all, delete-orphan")
    
    # 관계 설정: github_account 테이블과 github_total_data 테이블 간의 1:N 관계
    github_total_data = relationship("GithubTotalData",
                                     back_populates="github_account")
    
    # 관계 설정: github_account 테이블과 github_score 테이블 간의 1:N 관계
    github_score = relationship("GithubScore",
                                back_populates="github_account")