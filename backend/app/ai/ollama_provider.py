import logging

import ollama

from app.ai.provider import LLMProvider
from app.core.config import settings

logger = logging.getLogger(__name__)


class OllamaProvider(LLMProvider):
    """LLM provider backed by Ollama."""

    def __init__(self):
        self.client = ollama.Client(host=settings.ollama_host)

    def generate_prompt(
        self,
        product_name: str,
        description: str,
    ) -> str:
        """
        Generate a professional product photography prompt.
        """

        system_prompt = """
You are an expert AI prompt engineer.

Create a highly detailed image-generation prompt for a product photograph.

Include:
- studio lighting
- realistic shadows
- premium commercial photography
- clean background
- ultra high quality
- DSLR photography
- product centered

Return ONLY the prompt.
"""

        user_prompt = f"""
Product Name:
{product_name}

Description:
{description}
"""

        try:
            response = self.client.chat(
                model=settings.ollama_model,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_prompt,
                    },
                ],
            )

            return response["message"]["content"].strip()

        except Exception:
            logger.exception("Failed to generate prompt from Ollama")
            raise