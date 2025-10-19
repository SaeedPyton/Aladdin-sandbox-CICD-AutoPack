
"""
Base Video Upload Provider Interface
YouTube Automation System v3.0

Copyright (c) 2025 Saeed Alaediny. All rights reserved.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

class UploadProvider(ABC):
    """
    Abstract Base Class for Video Upload Providers.
    Defines the interface for interacting with different video upload services (e.g., YouTube API).
    """

    def __init__(self, provider_name: str, api_key: Optional[str] = None, **kwargs):
        self.provider_name = provider_name
        self.api_key = api_key

    @abstractmethod
    async def upload_video(self, video_path: str, title: str, description: str, tags: Optional[List[str]] = None, category: Optional[str] = None, privacy_status: str = "private", **kwargs) -> Dict[str, Any]:
        """
        Uploads a video to the specified platform.

        Args:
            video_path (str): Local path to the video file.
            title (str): Title of the video.
            description (str): Description of the video.
            tags (Optional[List[str]]): List of tags for the video.
            category (Optional[str]): Category of the video.
            privacy_status (str): Privacy status (e.g., "public", "private", "unlisted").
            **kwargs: Additional parameters specific to the upload provider.

        Returns:
            Dict[str, Any]: A dictionary containing upload status, video ID, and URL.
        """
        pass

    async def health_check(self) -> bool:
        """
        Performs a health check on the upload provider.

        Returns:
            bool: True if the provider is healthy, False otherwise.
        """
        return True # Default to healthy for stub/mock implementations

from typing import List

