from fastapi import APIRouter
from app.models.competitor import CompetitorRequest
from app.services.competitor import analyze_competitor

router = APIRouter()


@router.post("/competitor-research")
def competitor_research(request: CompetitorRequest):
    result = analyze_competitor(
        request.company,
        request.industry,
        request.country
    )

    return result