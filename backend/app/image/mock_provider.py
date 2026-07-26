from app.image.provider import ImageProvider
from app.utils.file_manager import (
    generate_image_filename,
    get_generated_image_path,
)


class MockImageProvider(ImageProvider):

    def generate_image(self, prompt: str) -> str:
        filename = generate_image_filename()

        path = get_generated_image_path(filename)

    
        path.write_bytes(b"")

        return f"/generated/{filename}"