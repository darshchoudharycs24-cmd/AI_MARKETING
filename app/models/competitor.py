from pydantic import BaseModel


class CompetitorRequest(BaseModel):
    company: str
    industry: str
    country: str