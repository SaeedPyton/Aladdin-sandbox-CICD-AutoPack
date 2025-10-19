
"""
Content Generation Service
YouTube Automation System v3.0

Copyright (c) 2025 Saeed Alaediny. All rights reserved.
"""

from typing import Dict, Any, Optional, List
from datetime import datetime

from providers.llm.factory import LLMProviderFactory

class ContentGeneratorService:
    """
    Content generation service.
    
    This service uses an LLM provider to generate video ideas and scripts.
    """
    
    def __init__(self, llm_provider_name: str = "mock", llm_model_name: str = "mock-llm-v1", llm_api_key: Optional[str] = None):
        """Initialize content generator with an LLM provider."""
        self.llm_provider = LLMProviderFactory.get_provider(
            name=llm_provider_name,
            model_name=llm_model_name,
            api_key=llm_api_key
        )
    
    async def generate_idea(self, niche: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """
        Generate a video idea using the LLM provider.
        
        Args:
            niche: Content niche
            **kwargs: Additional parameters
            
        Returns:
            dict: Video idea with title and description
        """
        if not niche:
            niche = "general knowledge"
        
        ideas = await self.llm_provider.generate_ideas(niche=niche, count=1, **kwargs)
        if ideas:
            return ideas[0]
        
        # Fallback if LLM provider returns no ideas
        return {
            "title": f"A New Video Idea for {niche}",
            "description": f"An automatically generated idea for a video in the {niche} category.",
            "tags": [niche, "generated"],
            "category": "Education",
            "estimated_duration": 600  # 10 minutes
        }
    
    async def generate_script(
        self,
        title: str,
        description: Optional[str] = None,
        duration: int = 300,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Generate a video script using the LLM provider.
        
        Args:
            title: Video title
            description: Video description
            duration: Target duration in seconds
            **kwargs: Additional parameters
            
        Returns:
            dict: Generated script with metadata
        """
        sections_to_generate = ["intro", "body", "outro"]
        generated_sections = await self.llm_provider.generate_script_sections(
            title=title,
            description=description or "",
            sections=sections_to_generate,
            **kwargs
        )
        
        intro = generated_sections.get("intro", "")
        body = generated_sections.get("body", "")
        outro = generated_sections.get("outro", "")
        
        script = f"{intro}\n\n{body}\n\n{outro}"
        
        return {
            "script": script,
            "word_count": len(script.split()),
            "estimated_duration": duration,
            "sections": generated_sections,
            "metadata": {
                "generated_at": datetime.utcnow().isoformat(),
                "provider": self.llm_provider.model_name,
                "model": self.llm_provider.model_name
            }
        }
    
    async def generate_complete_video_content(
        self,
        niche: Optional[str] = None,
        duration: int = 300,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Generate complete video content (idea + script) using the LLM provider.
        
        Args:
            niche: Content niche
            duration: Target duration in seconds
            **kwargs: Additional parameters
            
        Returns:
            dict: Complete video content
        """
        # Generate idea
        idea = await self.generate_idea(niche=niche, **kwargs)
        
        # Generate script
        script_data = await self.generate_script(
            title=idea["title"],
            description=idea["description"],
            duration=duration,
            **kwargs
        )
        
        return {
            **idea,
            **script_data,
            "status": "generated",
            "generated_at": datetime.utcnow().isoformat()
        }


