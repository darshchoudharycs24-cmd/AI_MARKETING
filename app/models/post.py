from pydantic import BaseModel
from typing import List
from typing import Optional


class PostRequest(BaseModel):
    company: str
    industry: str
    country: str
    platform: str = "LinkedIn"


class PostResponse(BaseModel):
    platform: str
    post_text: str
    caption: str
    hashtags: List[str]
    image_prompt: str
    image_url: Optional[str] = None