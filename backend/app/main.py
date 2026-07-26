import logging
import time

from fastapi import FastAPI, Request

from app.api.router import api_router
from app.core.config import settings
from app.core.logging import configure_logging
from fastapi.staticfiles import StaticFiles
configure_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
)
app.mount(
    "/generated",
    StaticFiles(directory="uploads/generated"),
    name="generated",
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    
    start_time = time.perf_counter()

    response = await call_next(request)

    duration_ms = (time.perf_counter() - start_time) * 1000

    logger.info(
        "%s %s | %s | %.2f ms",
        request.method,
        request.url.path,
        response.status_code,
        duration_ms,
    )

    return response


app.include_router(api_router)