# GitHub Collector Microservice

이 프로젝트는 사용자들의 GitHub 활동 데이터를 주기적으로 수집하고 저장하는 **마이크로서비스형 수집기 시스템**입니다.

FastAPI 기반의 경량 REST API 서버로 동작하며, 외부 서비스(예: 커뮤니티 백엔드)로부터 사용자 GitHub ID를 입력받아 저장소, 커밋 등 활동 정보를 GitHub API를 통해 수집합니다.

## 주요 특징

- **FastAPI 기반 경량 REST 서버**
- **주기적 스케줄링 수집 로직 내장**
- **MySQL 연동 및 SQLAlchemy ORM 사용**
- **streaming + batch 방식으로 메모리 효율적 수집**
- **외부에서 사용자 등록/삭제 API 제공**
- **데이터 제공 API를 통해 통합 시스템 연동 가능**

## 활용 예시

- 학교 커뮤니티 플랫폼과 연동하여 학생 GitHub 활동 점수 계산
- 별도 사용자 인증 없이 GitHub ID만으로 독립 운영 가능
- 여러 학교나 기관에서 재사용 가능한 마이크로서비스 형태로 배포

## 기술 스택

- Python 3.11
- FastAPI
- SQLAlchemy
- MySQL 8.x (Docker 기반 개발 환경 제공)
- Uvicorn (ASGI 서버)
- Docker / docker-compose
