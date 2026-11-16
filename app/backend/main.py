
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.backend.routes import router

app = FastAPI(
    title="MedQuery AI",
    description=(
        "Evidence-grounded Medical Question Answering "
        "using Retrieval-Augmented Generation."
    ),
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

app.include_router(
    router,
    prefix="/api/v1",
    tags=["Medical Question Answering"]
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to MedQuery AI",
        "documentation": "/docs",
        "api_status": "running"
    }
