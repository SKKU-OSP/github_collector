from sqlalchemy import Column, BigInteger, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Commit(Base):
    __tablename__ = "commit"

    sha = Column(String(40), primary_key=True, index=True) # 40자 고정길이 해쉬값
    repo_id = Column(BigInteger, ForeignKey("repository.repo_id"), nullable=False)
    addiction = Column(Integer, nullable=False)
    deletion = Column(Integer, nullable=False)
    author_date = Column(DateTime, nullable=False) # 커밋 작성자 시간
    committer_date = Column(DateTime, nullable=False) # 푸시 시간
    message = Column(Text, nullable=False)
    branch = Column(String(255), nullable=False)

    # 관계 설정: repository 테이블과 commit 테이블 간의 1:N 관계
    repository = relationship("Repository", back_populates="commits")