from app.ai.provider import LLMProvider


class MockLLMProvider(LLMProvider):
    """Mock LLM provider used for deployments and testing."""

    def generate_prompt(
        self,
        product_name: str,
        description: str,
    ) -> str:
        return (
            f"Professional studio product photography of {product_name}. "
            f"{description}. White background, soft lighting, "
            f"high quality, commercial product shot."
        )