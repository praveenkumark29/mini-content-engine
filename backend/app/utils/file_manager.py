import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import HTTPException, UploadFile

UPLOAD_DIR = Path("uploads")
GENERATED_DIR = UPLOAD_DIR / "generated"

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
GENERATED_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png",
    "webp",
}


def save_image(file: UploadFile) -> str:
    """ Save a user uploaded image. """

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No filename provided.",
        )

    extension = file.filename.rsplit(".", 1)[-1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported image format.",
        )

    filename = f"{uuid4()}.{extension}"

    destination = UPLOAD_DIR / filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return str(destination)


def generate_image_filename(extension: str = ".png") -> str:
    

    return f"{uuid4().hex}{extension}"


def get_generated_image_path(filename: str) -> Path:
    

    return GENERATED_DIR / filename