from uuid import UUID

from sqlalchemy.orm import Session

from app.models.job import Job


class JobRepository:
    """Repository responsible for job database operations."""

    def __init__(self, db: Session):
        self.db = db

    def create(self, job: Job) -> Job:
        """Persist a new job."""
        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)
        return job

    def get_by_id(self, job_id: UUID) -> Job | None:
        """Fetch a job by its ID."""
        return (
            self.db.query(Job)
            .filter(Job.id == job_id)
            .first()
        )

    def list(self) -> list[Job]:
        """all jobs."""
        return (
            self.db.query(Job)
            .order_by(Job.created_at.desc())
            .all()
        )

    def update(self, job: Job) -> Job:
        
        self.db.commit()
        self.db.refresh(job)
        return job

    def delete(self, job: Job) -> None:
        
        self.db.delete(job)
        self.db.commit()