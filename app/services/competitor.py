import os
import json
import time

from dotenv import load_dotenv
from google import genai

from app.prompts.competitor import competitor_prompt
from app.models.competitor import CompetitorResponse


# Load environment variables
load_dotenv()


# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# Models tried in order
MODELS = [
    "gemini-3.6-flash",
    "gemini-flash-latest",
    "gemini-3.5-flash",
    "gemini-3.5-flash-lite",
    "gemini-2.5-flash-lite"
]


def analyze_competitor(company, industry, country):

    # Build prompt
    prompt = competitor_prompt(
        company,
        industry,
        country
    )


    last_error = None


    # Try each model
    for model in MODELS:

        # Retry same model twice
        for attempt in range(2):

            try:

                print(
                    f"Trying Gemini model: {model} "
                    f"(attempt {attempt + 1})"
                )


                response = client.models.generate_content(

                    model=model,

                    contents=prompt,

                    config={
                        "response_mime_type": "application/json",
                        "response_schema": CompetitorResponse,
                    }
                )


                result = json.loads(response.text)


                print(
                    f"Success using model: {model}"
                )


                return result


            except Exception as e:

                last_error = e

                print(
                    f"Failed using {model}:"
                )

                print(e)


                # wait before retrying
                time.sleep(2)



    # If every model fails
    raise RuntimeError(
        f"All Gemini models failed. Last error: {last_error}"
    )