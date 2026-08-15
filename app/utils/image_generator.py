import os
import base64
from uuid import uuid4
from pathlib import Path

from dotenv import load_dotenv
from google import genai


# Load environment variables
load_dotenv()


# Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# Image output directory
IMAGE_DIR = Path("frontend/generated_images")
IMAGE_DIR.mkdir(parents=True, exist_ok=True)


IMAGE_MODEL = "gemini-3.1-flash-image"


def generate_post_image(image_prompt: str) -> str | None:

    try:

        print("Generating image with Gemini...")
        print("Prompt:", image_prompt)

        response = client.models.generate_content(
            model=IMAGE_MODEL,
            contents=image_prompt,
            config={
                "response_modalities": ["IMAGE"]
            }
        )

        image_data = None

        # Find generated image
        for part in response.parts:

            if part.inline_data is not None:
                image_data = part.inline_data.data
                break

        if image_data is None:
            print("Gemini did not return an image.")
            return None

        # Generate filename
        filename = f"post_{uuid4().hex}.png"

        filepath = IMAGE_DIR / filename

        # Save image
        if isinstance(image_data, bytes):
            image_bytes = image_data
        else:
            image_bytes = base64.b64decode(image_data)

        with open(filepath, "wb") as f:
            f.write(image_bytes)

        print(f"Image saved to: {filepath}")

        # URL used by frontend
        return f"/generated-images/{filename}"

    except Exception as e:

        print("IMAGE GENERATION ERROR:")
        print(str(e))

        # Do NOT crash the entire post-generation request
        return None