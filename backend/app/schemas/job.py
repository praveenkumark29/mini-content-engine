from uuid import UUID

from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    product_name: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)


class JobCreateResponse(BaseModel):
    id: UUID
    status: str


class JobStatusResponse(BaseModel):
    
    id: UUID
    product_name: str
    status: str
    output_image: str | None = None

class HealthResponse(BaseModel):
    """Health endpoint response."""

    status: str
    database: str
    version: str