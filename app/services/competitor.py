import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_competitor(company, industry, country):
    prompt = f"""
    Analyze the company {company}.
    Industry: {industry}
    Country: {country}

    Give a short competitor analysis.
    """

    response = client.models.generate_content(
    model="models/gemini-flash-latest",
    contents=prompt

    )

    return {
        "analysis": response.text
    }