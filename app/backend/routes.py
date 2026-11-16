
from fastapi import APIRouter
from app.backend.schemas import QuestionRequest, QuestionResponse

router = APIRouter()

DISCLAIMER = (
    "MedQuery AI is an academic research prototype. "
    "It does not replace professional medical advice."
)


@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "application": "MedQuery AI",
        "version": "0.1.0"
    }


@router.post("/ask", response_model=QuestionResponse)
async def ask_question(request: QuestionRequest):

    return QuestionResponse(
        question=request.question,
        answer=(
            "The medical question has been received. "
            "The evidence retrieval and answer generation "
            "pipeline is being developed."
        ),
        sources=[],
        status="pipeline_pending",
        disclaimer=DISCLAIMER
    )
