from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.project import ProjectRead, ProjectArchive
from app.services.project import archive_project
from app.db.session import get_db

router = APIRouter()

@router.get("/projects", response_model=list[ProjectRead])
def read_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).all()
    return projects

@router.patch("/projects/{project_id}/archive", response_model=ProjectRead)
def archive_project_endpoint(
    project_id: int,
    archive_data: ProjectArchive,
    db: Session = Depends(get_db)
):
    if not archive_data.is_archived:
        raise HTTPException(
            status_code=400,
            detail="Cannot unarchive projects through this endpoint"
        )
    return archive_project(db, project_id)