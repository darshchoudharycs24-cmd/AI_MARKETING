def post_prompt(company, industry, country, platform="LinkedIn"):

    return f"""
You are an expert social media marketing strategist.

Create a high-quality, ready-to-publish social media post for:

Company: {company}
Industry: {industry}
Country/Market: {country}
Platform: {platform}

The post must be suitable for direct publishing by the company.

Requirements:

1. Create original and engaging post content.
2. The content must be relevant to the company's industry.
3. Do not make unsupported factual claims.
4. Do not copy competitors.
5. Use a professional but engaging tone.
6. Include a clear marketing objective.
7. Include a natural call-to-action.
8. Generate 5-8 relevant hashtags.
9. Create a detailed image prompt for an accompanying professional
   marketing image.
10. The image prompt should describe a visually appealing image
    without putting large amounts of text inside the image.
11. The final result must be ready to post with minimal or no editing.

Return ONLY valid JSON in exactly this structure:

{{
    "platform": "{platform}",
    "post_text": "The complete post text ready for publishing",
    "caption": "A short caption suitable for the post",
    "hashtags": [
        "#example",
        "#marketing",
        "#business"
    ],
    "image_prompt": "Detailed prompt for generating the accompanying image"
}}
"""