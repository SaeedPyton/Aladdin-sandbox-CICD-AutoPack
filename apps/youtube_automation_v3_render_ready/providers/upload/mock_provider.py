
"""
Mock Video Upload Provider Implementation
YouTube Automation System v3.0

Copyright (c) 2025 Saeed Alaediny. All rights reserved.
"""

import random
import time
from typing import Dict, Any, Optional, List

from .base import UploadProvider

class MockUploadProvider(UploadProvider):
    """
    A mock implementation of the UploadProvider for testing and development.
    """

    def __init__(self, provider_name: str = "mock-upload-v1", api_key: Optional[str] = None, **kwargs):
        super().__init__(provider_name, api_key, **kwargs)

    async def upload_video(self, video_path: str, title: str, description: str, tags: Optional[List[str]] = None, category: Optional[str] = None, privacy_status: str = "private", **kwargs) -> Dict[str, Any]:
        """
        Mocks video upload.
        """
        print(f"MockUploadProvider: Uploading video from {video_path} with title: {title}")
        
        # Simulate some processing time
        await self._simulate_async_delay()

        video_id = f"mock_upload_{int(time.time())}_{random.randint(1000, 9999)}"
        mock_video_url = f"https://mock-youtube.com/watch?v={video_id}"

        return {
            "video_id": video_id,
            "status": "uploaded",
            "url": mock_video_url,
            "title": title,
            "description": description,
            "tags": tags,
            "category": category,
            "privacy_status": privacy_status,
            "uploaded_at": datetime.utcnow().isoformat(),
            "provider": self.provider_name
        }

    async def _simulate_async_delay(self, min_delay: float = 0.5, max_delay: float = 2.0):
        """
        Simulates an asynchronous delay.
        """
        await asyncio.sleep(random.uniform(min_delay, max_delay))

from datetime import datetime
import asyncio

