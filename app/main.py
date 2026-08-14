from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.api.competitor import router as competitor_router


app = FastAPI(
    title="AI Marketing Platform",
    description="Backend API for AI Marketing Internship Project",
    version="1.0.0"
)


# Register API routes

app.include_router(competitor_router)


# Serve frontend files

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


@app.get("/")
def root():
    return FileResponse("frontend/index.html")