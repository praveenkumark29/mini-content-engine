from app.image.provider import ImageProvider


class ComfyUIProvider(ImageProvider):
    
    def generate_image(
        self,
        prompt: str,
    ) -> str:
        raise NotImplementedError(
            "ComfyUI provider not implemented yet."
        )