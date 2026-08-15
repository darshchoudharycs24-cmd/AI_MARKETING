from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.api.competitor import router as competitor_router
from app.api.post import router as post_router


app = FastAPI(
    title="AI Marketing Platform",
    description="Backend API for AI Marketing Internship Project",
    version="1.0.0"
)


# Register API routes

app.include_router(competitor_router)
app.include_router(post_router)


# Serve frontend files

app.mount(
    "/frontend",
    StaticFiles(directory="frontend"),
    name="frontend"
)


# Serve generated post images

app.mount(
    "/generated-images",
    StaticFiles(directory="frontend/generated_images"),
    name="generated-images"
)


@app.get("/")
def root():
    return FileResponse("frontend/index.html")