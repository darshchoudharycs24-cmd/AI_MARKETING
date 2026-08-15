import os
import json

from dotenv import load_dotenv
from google import genai

from app.prompts.post import post_prompt
from app.models.post import PostResponse
from app.utils.image_generator import generate_post_image


load_dotenv()


# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


MODEL_NAME = "gemini-3.6-flash"


def generate_marketing_post(
    company,
    industry,
    country,
    platform="LinkedIn"
):

    # Build the post-generation prompt
    prompt = post_prompt(
        company,
        industry,
        country,
        platform
    )

    # Ask Gemini to create the post
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": PostResponse,
        }
    )

    # Convert Gemini response to Python dictionary
    result = json.loads(response.text)

    # Generate the accompanying image
    image_url = generate_post_image(
        result["image_prompt"]
    )

    # Add generated image URL to the response
    result["image_url"] = image_url

    return result