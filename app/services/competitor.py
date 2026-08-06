import os
from dotenv import load_dotenv
from google import genai

from app.prompts.competitor import competitor_prompt

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
        contents=prompt
    )

    # Return AI response
    return {
    "company": company,
    "industry": industry,
    "country": country,
    "analysis": response.text
}