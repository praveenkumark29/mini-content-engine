from app.image.provider import ImageProvider


class BedrockProvider(ImageProvider):
    

    def generate_image(
        self,
        prompt: str,
    ) -> str:
        raise NotImplementedError(
            "Bedrock provider not implemented yet."
        )