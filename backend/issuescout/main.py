from fastapi import FastAPI

from issuescout.api.v1.routes import router

app = FastAPI(
    title="IssueScout API",
    version="0.1.0",
    description="GitHub Contribution Assistant",
)


@app.get("/")
async def root():
    return {"message": "Welcome to IssueScout 🚀"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


app.include_router(router)