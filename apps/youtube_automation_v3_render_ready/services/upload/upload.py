
"""
Video Uploader Service
YouTube Automation System v3.0

Copyright (c) 2025 Saeed Alaediny. All rights reserved.
"""

from typing import Dict, Any, Optional, List

from providers.upload.factory import UploadProviderFactory

class UploaderService:
    """
    Video uploading service.
    
    This service uses an Upload provider to upload videos to platforms like YouTube.
    """
    
    def __init__(self, upload_provider_name: str = "mock", upload_api_key: Optional[str] = None):
        """Initialize uploader with an Upload provider."""
        self.upload_provider = UploadProviderFactory.get_provider(
            name=upload_provider_name,
            api_key=upload_api_key
        )
    
    async def upload_video(self, video_path: str, title: str, description: str, tags: Optional[List[str]] = None, category: Optional[str] = None, privacy_status: str = "private", **kwargs) -> Dict[str, Any]:
        """
        Uploads a video using the Upload provider.
        
        Args:
            video_path (str): Local path to the video file.
            title (str): Title of the video.
            description (str): Description of the video.
            tags (Optional[List[str]]): List of tags for the video.
            category (Optional[str]): Category of the video.
            privacy_status (str): Privacy status (e.g., "public", "private", "unlisted").
            **kwargs: Additional parameters.
            
        Returns:
            Dict[str, Any]: A dictionary containing upload status, video ID, and URL.
        """
        print(f"UploaderService: Requesting video upload from {self.upload_provider.provider_name} for {video_path}...")
        upload_data = await self.upload_provider.upload_video(
            video_path=video_path,
            title=title,
            description=description,
            tags=tags,
            category=category,
            privacy_status=privacy_status,
            **kwargs
        )
        return upload_data


