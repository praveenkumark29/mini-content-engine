from app.core.config import settings


def build_file_url(path: str) -> str:
    return f"{settings.base_url}{path}"