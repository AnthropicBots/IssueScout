from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from issuescout.api.v1.routes import router
from issuescout.core.config import settings
from issuescout.core.exceptions import (
    register_exception_handlers,
)
from issuescout.middleware import (
    logging_middleware,
)
from issuescout.models.responses import (
    HealthResponse,
    RootResponse,
)
from issuescout.core.logging import LOGGER_NAME
from issuescout.api.v1.docs.tags import (
    GENERAL_TAG,
)
from issuescout import __version__

app = FastAPI(
    title="IssueScout API",
    summary=("GitHub contribution assistant for discovering and analyzing issues."),
    description=(
        "IssueScout analyzes GitHub repositories, issues, "
        "pull requests, commits, comments, and repository "
        "metadata to help contributors discover suitable "
        "issues and understand their relationships."
    ),
    version=__version__,
    contact={
        "name": "Bhuvansh Kataria",
        "url": "https://github.com/BHUVANSH855",
    },
    license_info={
        "name": "MIT License",
    },
)
register_exception_handlers(app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.middleware("http")(
    logging_middleware,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

logging.getLogger(LOGGER_NAME)


@app.get(
    "/",
    response_model=RootResponse,
    summary="Welcome",
    tags=[GENERAL_TAG],
)
async def root():
    return RootResponse(
        name="IssueScout API",
        version=app.version,
        docs="/docs",
        openapi="/openapi.json",
        health="/health",
    )


@app.get(
    "/health",
    response_model=HealthResponse,
    summary="Health Check",
    tags=[GENERAL_TAG],
)
async def health():
    return HealthResponse(
        status="healthy",
        service="IssueScout API",
        version=app.version,
    )


app.include_router(
    router,
    prefix="/api/v1",
)
