import os
import json
from dotenv import load_dotenv
from google import genai

from app.prompts.competitor import competitor_prompt
from app.models.competitor import CompetitorResponse

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Model to use
MODEL_NAME = "models/gemini-flash-latest"


def analyze_competitor(company, industry, country):
    # Build the prompt
    prompt = competitor_prompt(
        company,
        industry,
        country
    )

    # Send prompt to Gemini
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": CompetitorResponse,
        }
    )

    # Return AI response

    result = json.loads(response.text)
    return result
