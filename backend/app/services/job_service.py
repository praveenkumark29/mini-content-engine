import logging
from uuid import UUID

from app.models.job import Job
from app.repositories.job_repository import JobRepository

logger = logging.getLogger(__name__)


class JobService:
    

    def __init__(self, repository: JobRepository):
        self.repository = repository

    def create_job(
        self,
        product_name: str,
        description: str,
    ) -> Job:
        

        logger.info(
            "Creating job for product '%s'",
            product_name,
        )

        job = Job(
            product_name=product_name,
            description=description,
            status="pending",
        )

        job = self.repository.create(job)

        logger.info(
            "Job %s created successfully",
            job.id,
        )

        return job

    def get_job(self, job_id: UUID) -> Job | None:
        
        logger.info("Fetching job %s", job_id)

        return self.repository.get_by_id(job_id)

    def list_jobs(self) -> list[Job]:
        
        logger.info("Fetching all jobs")

        return self.repository.list()

    def update_job(self, job: Job) -> Job:
        
        logger.info("Updating job %s", job.id)

        updated_job = self.repository.update(job)

        logger.info("Job %s updated successfully", job.id)

        return updated_job

    def delete_job(self, job: Job) -> None:
        
        logger.info("Deleting job %s", job.id)

        self.repository.delete(job)

        logger.info("Job %s deleted successfully", job.id)