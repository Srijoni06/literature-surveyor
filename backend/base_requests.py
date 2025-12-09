from typing import Literal
from pydantic import BaseModel, Field, field_validator

# Request Classes


class GenerateContentRequest(BaseModel):
    """Request model for generating content."""

    question: str = Field(..., description="question for content generation")
    local_llm: bool = Field(False, description="Whether to use a local LLM (default: False)")

    @field_validator("question")
    def validate_question(cls, value: str) -> str:
        """Ensure question is not empty."""
        if not value.strip():
            raise ValueError("question cannot be empty")
        return value.strip()


# Response Classes


class GenerateContentResponse(BaseModel):
    """Response model for content generation."""

    originalQuestion: str = Field(..., description="Status of the content generation")
    providerUsed: Literal["mistral", "gemini"] = Field(..., description="Message about the content generation")
    usedLocalLLM: bool = Field(..., description="Local LLM or not")
    answer: str = Field(..., description="Generated content")

    @field_validator("answer")
    def validate_data(cls, value: str) -> str:
        """Ensure data is not empty."""
        if not value.strip():
            raise ValueError("Generated content cannot be empty")
        return value.strip()