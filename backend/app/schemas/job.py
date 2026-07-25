from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class GenerateJobRequest(BaseModel):
    
    product_name: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Product name",
    )
    description: str = Field(
        ...,
        min_length=1,
        description="Product description",
    )


class JobResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    product_name: str
    description: str
    status: str
    prompt: str | None = None
    input_image: str | None = None
    output_image: str | None = None
    created_at: datetime
    updated_at: datetime


class JobStatusResponse(BaseModel):
    
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    status: str


class HealthResponse(BaseModel):
    """Health endpoint response."""

    status: str
    database: str
    version: str