from pydantic import BaseModel
from typing import List


class CompetitorRequest(BaseModel):
    company: str
    industry: str
    country: str


class SocialMediaStrategy(BaseModel):
    main_platforms: List[str]
    posting_frequency: str
    content_themes: List[str]
    brand_tone: str
    cta_style: str
    visual_style: str


class Competitor(BaseModel):
    name: str
    description: str
    industry: str
    target_audience: str
    social_media_strategy: SocialMediaStrategy


class MarketingStrategy(BaseModel):
    strengths: List[str]
    weaknesses: List[str]
    opportunities: List[str]
    content_gaps: List[str]
    suggestions: List[str]


class CompetitorResponse(BaseModel):
    company: str
    competitors: List[Competitor]
    marketing_strategy: MarketingStrategy
    summary: str
    