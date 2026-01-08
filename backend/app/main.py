from fastapi import FastAPI
from app.api.v1.endpoints import projects
from app.db.session import get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Project Tracker API", description="Immutable API for project tracking")

# Add CORS middleware for frontend compatibility
cors = CORSMiddleware(
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(CORSMiddleware, **cors.__dict__)

# Include versioned router
app.include_router(projects.router, prefix="/api/v1")

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}