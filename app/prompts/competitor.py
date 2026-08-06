def competitor_prompt(company, industry, country):
    return f"""
You are an expert market research analyst.

Analyze the company {company} in the {industry} industry in {country}.

Provide the following:

1. Company Overview
2. Top Competitors
3. Competitor Strengths
4. Competitor Weaknesses
5. Market Opportunities
6. Strategic Recommendations

Keep the response clear, professional, and well-structured.
"""