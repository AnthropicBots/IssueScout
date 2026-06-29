from fastapi import FastAPI

from issuescout.api.v1.routes import router

app = FastAPI(
    title="IssueScout API",
    summary=(
        "GitHub contribution assistant for "
        "discovering and analyzing issues."
    ),
    description=(
        "IssueScout analyzes GitHub repositories, issues, "
        "pull requests, commits, comments, and repository "
        "metadata to help contributors discover suitable "
        "issues and understand their relationships."
    ),
    version="0.1.0",
    contact={
        "name": "Bhuvansh Kataria",
        "url": "https://github.com/BHUVANSH855",
    },
    license_info={
        "name": "MIT License",
    },
)


@app.get(
    "/",
    summary="Welcome",
    tags=["General"],
)
async def root():
    return {
        "message": "Welcome to IssueScout 🚀",
    }


@app.get(
    "/health",
    summary="Health Check",
    tags=["General"],
)
async def health():
    return {
        "status": "healthy",
    }


app.include_router(router)