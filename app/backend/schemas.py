
from pydantic import BaseModel, Field
from typing import Optional


class QuestionRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=5,
        max_length=2000,
        description="Medical question submitted by the user"
    )


class SourceReference(BaseModel):
    source_id: str
    title: str
    content: Optional[str] = None


class QuestionResponse(BaseModel):
    question: str
    answer: str
    sources: list[SourceReference] = []
    status: str
    disclaimer: str
