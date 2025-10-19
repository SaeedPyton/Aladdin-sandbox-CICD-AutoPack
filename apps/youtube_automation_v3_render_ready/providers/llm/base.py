
"""
Base LLM Provider Interface
YouTube Automation System v3.0

Copyright (c) 2025 Saeed Alaediny. All rights reserved.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional

class LLMProvider(ABC):
    """
    Abstract Base Class for LLM Providers.
    Defines the interface for interacting with different Large Language Models.
    """

    def __init__(self, model_name: str, api_key: Optional[str] = None, **kwargs):
        self.model_name = model_name
        self.api_key = api_key

    @abstractmethod
    async def generate_text(self, prompt: str, max_tokens: int = 500, temperature: float = 0.7, **kwargs) -> str:
        """
        Generates text based on a given prompt.

        Args:
            prompt (str): The input prompt for text generation.
            max_tokens (int): The maximum number of tokens to generate.
            temperature (float): Controls the randomness of the output. Higher values mean more random.
            **kwargs: Additional parameters specific to the LLM provider.

        Returns:
            str: The generated text.
        """
        pass

    @abstractmethod
    async def generate_ideas(self, niche: str, count: int = 3, **kwargs) -> List[Dict[str, Any]]:
        """
        Generates video ideas based on a niche.

        Args:
            niche (str): The content niche.
            count (int): The number of ideas to generate.
            **kwargs: Additional parameters.

        Returns:
            List[Dict[str, Any]]: A list of generated ideas, each with title and description.
        """
        pass

    @abstractmethod
    async def generate_script_sections(self, title: str, description: str, sections: List[str], **kwargs) -> Dict[str, str]:
        """
        Generates specific sections of a video script.

        Args:
            title (str): The video title.
            description (str): The video description.
            sections (List[str]): A list of section names to generate (e.g., ['intro', 'body', 'outro']).
            **kwargs: Additional parameters.

        Returns:
            Dict[str, str]: A dictionary where keys are section names and values are generated content.
        """
        pass

    async def health_check(self) -> bool:
        """
        Performs a health check on the LLM provider.

        Returns:
            bool: True if the provider is healthy, False otherwise.
        """
        return True # Default to healthy for stub/mock implementations


