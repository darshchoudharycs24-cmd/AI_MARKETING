from fastapi import FastAPI
from app.api.competitor import router as competitor_router

app = FastAPI(
    title="AI Marketing Platform",
    description="Backend API for AI Marketing Internship Project",
    version="1.0.0"
)

# Register Competitor API
app.include_router(competitor_router)

@app.get("/")
def root():
    return {
        "message": "AI Marketing Platform is running!"
    }