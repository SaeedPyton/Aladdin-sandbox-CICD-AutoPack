
"""
Video Builder Service
YouTube Automation System v3.0

Copyright (c) 2025 Saeed Alaediny. All rights reserved.
"""

from typing import Dict, Any, Optional, List

from providers.video.factory import VideoProviderFactory

class VideoBuilderService:
    """
    Video building service.
    
    This service uses a Video provider to generate videos from scripts.
    """
    
    def __init__(self, video_provider_name: str = "mock", video_api_key: Optional[str] = None):
        """Initialize video builder with a Video provider."""
        self.video_provider = VideoProviderFactory.get_provider(
            name=video_provider_name,
            api_key=video_api_key
        )
    
    async def build_video(self, script: str, voice_id: Optional[str] = None, background_music: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """
        Builds a video using the Video provider.
        
        Args:
            script (str): The full script for the video.
            voice_id (Optional[str]): Identifier for the voice to be used.
            background_music (Optional[str]): Path or identifier for background music.
            **kwargs: Additional parameters.
            
        Returns:
            Dict[str, Any]: A dictionary containing video URL, status, and other metadata.
        """
        print(f"VideoBuilderService: Requesting video generation from {self.video_provider.provider_name}...")
        video_data = await self.video_provider.generate_video(
            script=script,
            voice_id=voice_id,
            background_music=background_music,
            **kwargs
        )
        return video_data

    async def get_available_voices(self) -> List[Dict[str, Any]]:
        """
        Retrieves available voices from the video provider.
        """
        return await self.video_provider.get_available_voices()

    async def get_available_background_music(self) -> List[Dict[str, Any]]:
        """
        Retrieves available background music from the video provider.
        """
        return await self.video_provider.get_available_background_music()


