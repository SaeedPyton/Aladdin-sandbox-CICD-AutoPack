
"""
Base Video Generation Provider Interface
YouTube Automation System v3.0

Copyright (c) 2025 Saeed Alaediny. All rights reserved.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List

class VideoProvider(ABC):
    """
    Abstract Base Class for Video Generation Providers.
    Defines the interface for interacting with different video generation services.
    """

    def __init__(self, provider_name: str, api_key: Optional[str] = None, **kwargs):
        self.provider_name = provider_name
        self.api_key = api_key

    @abstractmethod
    async def generate_video(self, script: str, voice_id: Optional[str] = None, background_music: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """
        Generates a video based on a given script.

        Args:
            script (str): The full script for the video.
            voice_id (Optional[str]): Identifier for the voice to be used.
            background_music (Optional[str]): Path or identifier for background music.
            **kwargs: Additional parameters specific to the video provider.

        Returns:
            Dict[str, Any]: A dictionary containing video URL, status, and other metadata.
        """
        pass

    @abstractmethod
    async def get_available_voices(self) -> List[Dict[str, Any]]:
        """
        Retrieves a list of available voices for video generation.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries, each describing a voice.
        """
        pass

    @abstractmethod
    async def get_available_background_music(self) -> List[Dict[str, Any]]:
        """
        Retrieves a list of available background music tracks.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries, each describing a music track.
        """
        pass

    async def health_check(self) -> bool:
        """
        Performs a health check on the video provider.

        Returns:
            bool: True if the provider is healthy, False otherwise.
        """
        return True # Default to healthy for stub/mock implementations


