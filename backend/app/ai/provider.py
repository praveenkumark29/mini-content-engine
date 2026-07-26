from abc import ABC, abstractmethod


class LLMProvider(ABC):
    

    @abstractmethod
    def generate_prompt(
        self,
        product_name: str,
        description: str,
    ) -> str:
        
        raise NotImplementedError