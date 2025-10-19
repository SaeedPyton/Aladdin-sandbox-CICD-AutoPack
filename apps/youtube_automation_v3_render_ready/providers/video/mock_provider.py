
"""
Mock Video Generation Provider Implementation
YouTube Automation System v3.0

Copyright (c) 2025 Saeed Alaediny. All rights reserved.
"""

import random
import time
from typing import Dict, Any, Optional, List

from .base import VideoProvider

class MockVideoProvider(VideoProvider):
    """
    A mock implementation of the VideoProvider for testing and development.
    """

    def __init__(self, provider_name: str = "mock-video-v1", api_key: Optional[str] = None, **kwargs):
        super().__init__(provider_name, api_key, **kwargs)
        self.mock_voices = [
            {"id": "mock-voice-1", "name": "Standard Male", "language": "en-US"},
            {"id": "mock-voice-2", "name": "Standard Female", "language": "en-US"},
            {"id": "mock-voice-3", "name": "Narrator", "language": "en-US"},
        ]
        self.mock_music = [
            {"id": "mock-music-1", "name": "Upbeat Corporate", "genre": "corporate"},
            {"id": "mock-music-2", "name": "Chill Ambient", "genre": "ambient"},
            {"id": "mock-music-3", "name": "Dramatic Orchestral", "genre": "orchestral"},
        ]

    async def generate_video(self, script: str, voice_id: Optional[str] = None, background_music: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """
        Mocks video generation.
        """
        print(f"MockVideoProvider: Generating video for script (first 100 chars): {script[:100]}...")
        print(f"Voice ID: {voice_id}, Background Music: {background_music}")
        
        # Simulate some processing time
        await self._simulate_async_delay()

        video_id = f"mock_video_{int(time.time())}_{random.randint(1000, 9999)}"
        mock_video_url = f"https://mock-video-cdn.com/{video_id}.mp4"

        return {
            "video_id": video_id,
            "status": "completed",
            "url": mock_video_url,
            "duration": len(script.split()) / 150 * 60, # Estimate 150 words per minute
            "created_at": datetime.utcnow().isoformat(),
            "provider": self.provider_name,
            "voice_used": voice_id or "default",
            "music_used": background_music or "none"
        }

    async def get_available_voices(self) -> List[Dict[str, Any]]:
        """
        Mocks retrieving available voices.
        """
        await self._simulate_async_delay()
        return self.mock_voices

    async def get_available_background_music(self) -> List[Dict[str, Any]]:
        """
        Mocks retrieving available background music.
        """
        await self._simulate_async_delay()
        return self.mock_music

    async def _simulate_async_delay(self, min_delay: float = 0.5, max_delay: float = 2.0):
        """
        Simulates an asynchronous delay.
        """
        await asyncio.sleep(random.uniform(min_delay, max_delay))

from datetime import datetime
import asyncio

