import os
from dotenv import load_dotenv

from app.utils.image_generator import generate_post_image

load_dotenv()

image_prompt = """
Create a professional social media marketing image for a productivity
software company.

Theme: Working smarter with AI.

Style:
- Modern
- Clean
- Premium
- Professional
- Suitable for LinkedIn
- Minimal text
- Blue and white visual theme
- No logos
- No copyrighted characters

The image should visually communicate productivity, organization,
and AI-assisted work.
"""

try:
    image_path = generate_post_image(image_prompt)

    print("IMAGE GENERATED SUCCESSFULLY")
    print("Saved at:", image_path)

except Exception as e:
    print("IMAGE GENERATION FAILED")
    print(type(e).__name__, ":", e)