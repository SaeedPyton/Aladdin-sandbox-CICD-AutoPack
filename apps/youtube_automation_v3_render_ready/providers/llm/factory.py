
"""
LLM Provider Factory
YouTube Automation System v3.0

Copyright (c) 2025 Saeed Alaediny. All rights reserved.
"""

from typing import Type

from .base import LLMProvider
from .mock_provider import MockLLMProvider
# from .ollama_provider import OllamaLLMProvider # Future integration
# from .openai_provider import OpenAILLMProvider # Future integration

class LLMProviderFactory:
    """
    Factory class to create instances of LLM providers.
    """

    _providers: Dict[str, Type[LLMProvider]] = {
        "mock": MockLLMProvider,
        # "ollama": OllamaLLMProvider,
        # "openai": OpenAILLMProvider,
    }

    @classmethod
    def register_provider(cls, name: str, provider_class: Type[LLMProvider]):
        """
        Registers a new LLM provider.
        """
        if not issubclass(provider_class, LLMProvider):
            raise ValueError("Provider class must inherit from LLMProvider")
        cls._providers[name] = provider_class

    @classmethod
    def get_provider(cls, name: str, model_name: str, api_key: Optional[str] = None, **kwargs) -> LLMProvider:
        """
        Retrieves an instance of the specified LLM provider.
        """
        provider_class = cls._providers.get(name.lower())
        if not provider_class:
            raise ValueError(f"Unknown LLM provider: {name}")
        return provider_class(model_name=model_name, api_key=api_key, **kwargs)


