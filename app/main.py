from fastapi import FastAPI

app = FastAPI(
    title="AI Marketing Platform",
    description="Backend API for AI Marketing Internship Project",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "AI Marketing Platform is running!"
    }