import logging

logger = logging.getLogger(__name__)


class PromptService:
    """Service for generating image promptss."""

    def generate_prompt(
        self,
        product_name: str,
        description: str,
    ) -> str:
        """
        Generate a prompt for the image generation model.
        """

        logger.info(
            "Generating prompt for product '%s'",
            product_name,
        )

        return f"""
Professional commercial product photography of {product_name}.

Description:
{description}

Soft lighting.
Luxury aesthetic.
Ultra realistic.
8K quality.
Lifestyle scene.
White background.
Product-focused composition.
""".strip()