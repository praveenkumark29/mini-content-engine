from app.image.factory import ImageFactory


class ImageService:

    def __init__(self):
        self.provider = ImageFactory.create()

    def generate_image(
        self,
        prompt: str,
        input_image: str,
    ) -> str:
        return self.provider.generate_image(
            prompt=prompt,
            input_image=input_image,
        )