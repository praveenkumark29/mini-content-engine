from uuid import UUID

from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
    File,
    Form,
    UploadFile,
    status,
)
from sqlalchemy.orm import Session

from app.core.exceptions import JobNotFoundException
from app.db.session import get_db
from app.repositories.job_repository import JobRepository
from app.schemas.job import JobCreateResponse, JobStatusResponse
from app.services.job_service import JobService

router = APIRouter(
    prefix="",
    tags=["Jobs"],
)


@router.post(
    "/generate",
    response_model=JobCreateResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
def generate_job(
    background_tasks: BackgroundTasks,
    product_name: str = Form(...),
    description: str = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    repository = JobRepository(db)
    service = JobService(repository)

    job = service.create_generation_job(
        db=db,
        background_tasks=background_tasks,
        product_name=product_name,
        description=description,
        image=image,
    )

    return JobCreateResponse(
        id=job.id,
        status=job.status,
    )


@router.get(
    "/jobs/{job_id}",
    response_model=JobStatusResponse,
)
def get_job_status(
    job_id: UUID,
    db: Session = Depends(get_db),
):
    repository = JobRepository(db)
    service = JobService(repository)

    job = service.get_job(job_id)

    if job is None:
        raise JobNotFoundException()

    return JobStatusResponse(
        id=job.id,
        product_name=job.product_name,
        status=job.status,
        output_image=job.output_image,
    )