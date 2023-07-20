import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from src.auth.jwt_auth import AuthHandler
from src.db.database import Base
from fastapi.testclient import TestClient

from src.db.models import Post
from src.main import app


@pytest.fixture(scope="module")
def test_db():
    engine = create_engine("postgresql://postgres:postgres@localhost/test_database")

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    Base.metadata.create_all(bind=engine)
    yield db

    db.close()


@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="module")
def test_token():
    auth_handler = AuthHandler()
    token = auth_handler.encode_token(user_id=1)
    return token


@pytest.fixture(scope="module")
def test_post(test_db: Session):
    post_data = {
        "content": "This is a test post"
    }
    post = Post(**post_data)
    test_db.add(post)
    test_db.commit()
    test_db.refresh(post)
    return post
