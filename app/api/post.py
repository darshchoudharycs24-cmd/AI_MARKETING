from fastapi import APIRouter, HTTPException

from app.models.post import PostRequest, PostResponse
from app.services.post import generate_marketing_post


router = APIRouter(
    prefix="/api/posts",
    tags=["Posts"]
)


@router.post("/generate", response_model=PostResponse)
def generate_post(request: PostRequest):

    try:
        result = generate_marketing_post(
            company=request.company,
            industry=request.industry,
            country=request.country,
            platform=request.platform
        )

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )