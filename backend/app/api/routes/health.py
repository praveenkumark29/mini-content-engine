import logging

from fastapi import APIRouter, HTTPException

from app.db.init_db import check_database
from app.schemas.job import HealthResponse

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get(
    "/",
    response_model=HealthResponse,
)
def health():
    """
    Application health check.
    """

    logger.info("Health endpoint accessed")

    database_connected = check_database()

    if not database_connected:
        logger.error("Database connectivity check failed")

        raise HTTPException(
            status_code=503,
            detail="Database unavailable",
        )

    return HealthResponse(
        status="healthy",
        database="connected",
        version="1.0.0",
    )