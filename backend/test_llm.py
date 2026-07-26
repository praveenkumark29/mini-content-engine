from app.ai.llm_service import LLMService

service = LLMService()

prompt = service.generate_prompt(
    product_name="Nike Air Max",
    description="Premium running shoes with breathable mesh and cushioned sole.",
)

print(prompt)