from app.ai.factory import LLMFactory


class LLMService:
    """High-level service for prompt generation."""

    def __init__(self):
        self.provider = LLMFactory.create()

    def generate_prompt(
        self,
        product_name: str,
        description: str,
    ) -> str:
        return self.provider.generate_prompt(
            product_name=product_name,
            description=description,
        )