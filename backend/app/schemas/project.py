from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    description: str | None = None

    class Config:
        orm_mode = True

class ProjectRead(BaseModel):
    id: int
    name: str
    description: str | None
    created_at: str  # datetime will be formatted as ISO string
    is_archived: bool

    class Config:
        orm_mode = True

class ProjectArchive(BaseModel):
    is_archived: bool

    class Config:
        orm_mode = True