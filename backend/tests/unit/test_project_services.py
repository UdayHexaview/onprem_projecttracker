from app.db.session import get_db
from app.services.project import archive_project
from app.models.project import Project
from sqlalchemy.orm import Session
from fastapi import HTTPException
import pytest


def test_archive_project_creates_idempotency(get_db: Session):
    # Create test project
    project = Project(name="Test Project", description="Test description")
    get_db.add(project)
    get_db.commit()
    get_db.refresh(project)

    # First archive
    archived_project = archive_project(get_db, project.id)
    assert archived_project.is_archived is True

    # Second archive (idempotency test)
    same_project = archive_project(get_db, project.id)
    assert same_project.is_archived is True
    assert same_project.updated_at == archived_project.updated_at

    get_db.rollback()


def test_archive_non_existent_project(get_db: Session):
    with pytest.raises(HTTPException) as exc_info:
        archive_project(get_db, 9999)
    assert exc_info.value.status_code == 404
