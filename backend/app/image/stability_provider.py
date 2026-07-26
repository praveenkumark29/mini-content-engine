from app.image.provider import ImageProvider


class StabilityProvider(ImageProvider):
    

    def generate_image(
        self,
        prompt: str,
    ) -> str:
        raise NotImplementedError(
            "Stability provider not implemented yet."
        )