import shutil
from pathlib import Path

from app.image.provider import ImageProvider
from app.utils.file_manager import (
    generate_image_filename,
    get_generated_image_path,
)


class MockImageProvider(ImageProvider):

    def generate_image(
        self,
        prompt: str,
        input_image: str,
    ) -> str:

        filename = generate_image_filename()

        destination = get_generated_image_path(filename)

        shutil.copy(Path(input_image), destination)

        return f"/generated/{filename}"