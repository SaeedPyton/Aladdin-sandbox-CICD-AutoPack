
"""
Mock LLM Provider Implementation
YouTube Automation System v3.0

Copyright (c) 2025 Saeed Alaediny. All rights reserved.
"""

import random
from typing import Dict, Any, List, Optional

from .base import LLMProvider

class MockLLMProvider(LLMProvider):
    """
    A mock implementation of the LLMProvider for testing and development.
    """

    def __init__(self, model_name: str = "mock-llm-v1", api_key: Optional[str] = None, **kwargs):
        super().__init__(model_name, api_key, **kwargs)
        self.sample_topics = [
            "The Future of Artificial Intelligence",
            "Top 10 Programming Tips for Beginners",
            "How to Build a Successful YouTube Channel",
            "The Science Behind Climate Change",
            "Exploring the Mysteries of Space",
            "Healthy Eating Habits for a Better Life",
            "The Evolution of Technology",
            "Understanding Cryptocurrency and Blockchain",
            "Travel Guide: Hidden Gems Around the World",
            "Productivity Hacks for Remote Workers"
        ]
        self.sample_script_parts = {
            "intro": [
                "Hello and welcome back to our channel!",
                "Hey everyone, thanks for tuning in!",
                "Welcome to another exciting episode!",
                "Greetings, viewers! Today we have something special for you."
            ],
            "body_template": [
                "In today's video, we'll explore {topic} and discover why it matters.",
                "Let's dive deep into {topic} and uncover some fascinating insights.",
                "We're going to break down {topic} in a way that's easy to understand.",
                "Join me as we investigate {topic} from multiple perspectives."
            ],
            "outro": [
                "Thanks for watching! Don't forget to like and subscribe!",
                "If you enjoyed this video, hit that like button and subscribe for more!",
                "That's all for today! See you in the next video!",
                "Thanks for your time! Leave your thoughts in the comments below!"
            ]
        }

    async def generate_text(self, prompt: str, max_tokens: int = 500, temperature: float = 0.7, **kwargs) -> str:
        """
        Mocks text generation.
        """
        # Simple mock response based on prompt
        if "idea" in prompt.lower():
            return f"Generated idea for: {prompt}. Topic: {random.choice(self.sample_topics)}"
        elif "script" in prompt.lower():
            topic = kwargs.get("topic", "a fascinating subject")
            return f"Generated script for: {topic}. Intro: {random.choice(self.sample_script_parts['intro'])}. Body: This is a detailed body about {topic}. Outro: {random.choice(self.sample_script_parts['outro'])}"
        return f"Mock generated text for prompt: {prompt}"

    async def generate_ideas(self, niche: str, count: int = 3, **kwargs) -> List[Dict[str, Any]]:
        """
        Mocks video idea generation.
        """
        ideas = []
        for _ in range(count):
            topic = random.choice(self.sample_topics)
            ideas.append({
                "title": topic,
                "description": f"An in-depth look at {topic.lower()} within the {niche} niche.",
                "tags": [niche, "education", "mock"],
                "category": "Mock Category",
                "estimated_duration": random.randint(300, 900)
            })
        return ideas

    async def generate_script_sections(self, title: str, description: str, sections: List[str], **kwargs) -> Dict[str, str]:
        """
        Mocks video script section generation.
        """
        generated_sections = {}
        for section in sections:
            if section == "intro":
                generated_sections["intro"] = random.choice(self.sample_script_parts["intro"])
            elif section == "body":
                body_content = random.choice(self.sample_script_parts["body_template"]).format(topic=title)
                # Add some filler content for the body
                filler = " "
                for i in range(random.randint(3, 7)):
                    filler += f"Point {i+1}: This is a mock discussion point about {title}. "
                generated_sections["body"] = body_content + filler
            elif section == "outro":
                generated_sections["outro"] = random.choice(self.sample_script_parts["outro"])
            else:
                generated_sections[section] = f"Mock content for {section} about {title}"
        return generated_sections


