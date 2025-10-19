
"""
Upload Provider Factory
YouTube Automation System v3.0

Copyright (c) 2025 Saeed Alaediny. All rights reserved.
"""

from typing import Type, Dict, Optional

from .base import UploadProvider
from .mock_provider import MockUploadProvider
# from .youtube_api_provider import YouTubeAPIUploadProvider # Future integration

class UploadProviderFactory:
    """
    Factory class to create instances of Upload providers.
    """

    _providers: Dict[str, Type[UploadProvider]] = {
        "mock": MockUploadProvider,
        # "youtube": YouTubeAPIUploadProvider,
    }

    @classmethod
    def register_provider(cls, name: str, provider_class: Type[UploadProvider]):
        """
        Registers a new Upload provider.
        """
        if not issubclass(provider_class, UploadProvider):
            raise ValueError("Provider class must inherit from UploadProvider")
        cls._providers[name] = provider_class

    @classmethod
    def get_provider(cls, name: str, api_key: Optional[str] = None, **kwargs) -> UploadProvider:
        """
        Retrieves an instance of the specified Upload provider.
        """
        provider_class = cls._providers.get(name.lower())
        if not provider_class:
            raise ValueError(f"Unknown Upload provider: {name}")
        return provider_class(provider_name=name, api_key=api_key, **kwargs)


