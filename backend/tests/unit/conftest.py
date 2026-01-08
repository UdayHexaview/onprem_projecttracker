import pytest
from sqlalchemy.orm import Session

from app.db.session import Base, engine, SessionLocal

@pytest.fixture(autouse=True)
def create_tables():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
