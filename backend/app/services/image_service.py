import logging

logger = logging.getLogger(__name__)


class ImageService:
    """Service for image generation."""

    def generate_image(self, prompt: str) -> str:
        
        logger.info("Generating placeholder image")

        
        return "https://picsum.photos/768"