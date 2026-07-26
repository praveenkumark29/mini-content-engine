from abc import ABC, abstractmethod


class ImageProvider(ABC):
    

    @abstractmethod
    def generate_image(
        self,
        prompt: str,
    ) -> str:
        """
        Generate an image from a prompt.

        Returns:
            URL or local path of the generated image.
        """
        raise NotImplementedError