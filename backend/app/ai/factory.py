from app.ai.mock_provider import MockLLMProvider
from app.ai.ollama_provider import OllamaProvider
from app.core.config import settings


class LLMFactory:
    

    @staticmethod
    def create():
        provider = settings.llm_provider.lower()

        if provider == "ollama":
            return OllamaProvider()

        if provider == "mock":
            return MockLLMProvider()

        raise ValueError(f"Unsupported LLM provider: {provider}")