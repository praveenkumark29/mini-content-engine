import logging
from uuid import UUID

from sqlalchemy.orm import Session

from app.repositories.job_repository import JobRepository
from app.services.image_service import ImageService
from app.services.prompt_service import PromptService

logger = logging.getLogger(__name__)


class GenerationWorker:
    
    def __init__(self, db: Session):
        self.db = db
        self.repository = JobRepository(db)
        self.prompt_service = PromptService()
        self.image_service = ImageService()

    def process_job(self, job_id: UUID) -> None:
        """
        Process a generation job.

        Workflow:
        1. Mark job as processing.
        2. Generate AI prompt.
        3. Generate image.
        4. Update database.
        """

        job = self.repository.get_by_id(job_id)

        if job is None:
            logger.error("Job %s not found.", job_id)
            return

        try:
            logger.info("Started processing job %s", job.id)

            
            job.status = "processing"
            self.repository.update(job)

            
            logger.info("Generating prompt...")

            prompt = self.prompt_service.generate_prompt(
                product_name=job.product_name,
                description=job.description,
            )

            job.prompt = prompt
            self.repository.update(job)

            logger.info("Prompt generated successfully.")

            
            
            logger.info("Generating image...")

            image_url = self.image_service.generate_image(prompt)

            logger.info("Image generated successfully.")

            
            job.output_image = image_url
            job.status = "completed"

            self.repository.update(job)

            logger.info("Job %s completed successfully.", job.id)

        except Exception as exc:
            logger.exception(
                "Failed to process job %s: %s",
                job.id,
                exc,
            )

            job.status = "failed"
            self.repository.update(job)