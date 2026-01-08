import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.session import engine, Base
from app.models.project import Project
from sqlalchemy.orm import Session


@pytest.fixture
def client():
    # Create the database and tables
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    # Clean up the database
    Base.metadata.drop_all(bind=engine)


def test_get_projects(client):
    # Test GET /projects
    response = client.get("/api/v1/projects")
    assert response.status_code == 200
    assert response.json() == []


def test_archive_project(client):
    # Create a test project
    project = Project(name="Test Project", description="Test description")
    with Session(engine) as db:
        db.add(project)
        db.commit()
        db.refresh(project)
    
    # First archive
    response = client.patch(f"/api/v1/projects/{project.id}/archive", json={"is_archived": True})
    assert response.status_code == 200
    data = response.json()
    assert data["is_archived"] is True
    created_at_first = data["created_at"]
    
    # Second archive (idempotency test)
    response = client.patch(f"/api/v1/projects/{project.id}/archive", json={"is_archived": True})
    assert response.status_code == 200
    data = response.json()
    assert data["is_archived"] is True
    assert data["created_at"] == created_at_first  # Ensure created_at hasn't changed


def test_archive_non_existent_project(client):
    response = client.patch("/api/v1/projects/9999/archive", json={"is_archived": True})
    assert response.status_code == 404