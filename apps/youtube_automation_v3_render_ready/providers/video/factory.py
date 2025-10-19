
"""
Video Provider Factory
YouTube Automation System v3.0

Copyright (c) 2025 Saeed Alaediny. All rights reserved.
"""

from typing import Type, Dict, Optional

from .base import VideoProvider
from .mock_provider import MockVideoProvider
# from .synthesia_provider import SynthesiaVideoProvider # Future integration
# from .d_id_provider import DIDVideoProvider # Future integration

class VideoProviderFactory:
    """
    Factory class to create instances of Video providers.
    """

    _providers: Dict[str, Type[VideoProvider]] = {
        "mock": MockVideoProvider,
        # "synthesia": SynthesiaVideoProvider,
        # "d-id": DIDVideoProvider,
    }

    @classmethod
    def register_provider(cls, name: str, provider_class: Type[VideoProvider]):
        """
        Registers a new Video provider.
        """
        if not issubclass(provider_class, VideoProvider):
            raise ValueError("Provider class must inherit from VideoProvider")
        cls._providers[name] = provider_class

    @classmethod
    def get_provider(cls, name: str, api_key: Optional[str] = None, **kwargs) -> VideoProvider:
        """
        Retrieves an instance of the specified Video provider.
        """
        provider_class = cls._providers.get(name.lower())
        if not provider_class:
            raise ValueError(f"Unknown Video provider: {name}")
        return provider_class(provider_name=name, api_key=api_key, **kwargs)


