from app.core.config import settings

from app.image.bedrock_provider import BedrockProvider
from app.image.comfyui_provider import ComfyUIProvider
from app.image.huggingface_provider import HuggingFaceProvider
from app.image.mock_provider import MockImageProvider
from app.image.stability_provider import StabilityProvider


class ImageFactory:
   

    @staticmethod
    def create():
        provider = settings.image_provider.lower()

        providers = {
            "mock": MockImageProvider,
            "comfyui": ComfyUIProvider,
            "huggingface": HuggingFaceProvider,
            "stability": StabilityProvider,
            "bedrock": BedrockProvider,
        }

        if provider not in providers:
            raise ValueError(
                f"Unsupported image provider: {provider}"
            )

        return providers[provider]()