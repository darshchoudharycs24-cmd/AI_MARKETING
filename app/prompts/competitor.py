def competitor_prompt(company, industry, country):
    return f"""
You are an expert market research and digital marketing analyst.

Analyze the company "{company}" in the "{industry}" industry in "{country}".

Your task is to identify the company's top competitors and analyze their
marketing and social media strategies.

For the top 5 competitors, provide the following information for EACH competitor:

1. Competitor Information
   - name
   - short description
   - industry
   - target audience

2. Social Media Analysis
   - main social media platforms
   - posting frequency
   - content themes
   - brand tone
   - CTA style
   - visual style

3. Overall Marketing Strategy
   Analyze the competitive landscape and provide:
   - strengths
   - weaknesses
   - opportunities
   - content gaps
   - suggestions

4. Summary
   Provide a concise summary of the key findings.
   Mention common competitor strategies, important content gaps,
   and the most useful recommendations.

Important instructions:
- Identify exactly 5 competitors where possible.
- Keep descriptions concise and useful.
- Do not write a long essay.
- Return only the requested information.
- Follow the response structure provided by the API.
"""