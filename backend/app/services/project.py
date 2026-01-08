from sqlalchemy.orm import Session
from app.models.project import Project
from fastapi import HTTPException
from datetime import datetime


def archive_project(db: Session, project_id: int) -> Project:
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # Idempotent branch – do NOT modify anything
    if project.is_archived:
        return project

    # First archive – set fields + manually update timestamp to trigger onupdate
    project.is_archived = True
    project.updated_at = datetime.utcnow()

    db.add(project)
    db.commit()
    db.refresh(project)
    return project
