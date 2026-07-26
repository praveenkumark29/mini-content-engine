from app.image.provider import ImageProvider


class HuggingFaceProvider(ImageProvider):
   

    def generate_image(
        self,
        prompt: str,
    ) -> str:
        raise NotImplementedError(
            "HuggingFace provider not implemented yet."
        )