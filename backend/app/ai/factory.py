from app.ai.ollama_provider import OllamaProvider
from app.core.config import settings


class LLMFactory:
    """Factory for creating LLM providers."""

    @staticmethod
    def create():
        provider = settings.llm_provider.lower()

        if provider == "ollama":
            return OllamaProvider()

        raise ValueError(f"Unsupported LLM provider: {provider}")