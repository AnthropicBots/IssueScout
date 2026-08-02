from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from issuescout.core.exceptions.github import (
    GitHubAuthenticationError,
    GitHubNotFoundError,
    GitHubRateLimitError,
)
from issuescout.core.exceptions.repository import (
    RepositoryNotFoundError,
)
from issuescout.core.logging import logger


def register_exception_handlers(
    app: FastAPI,
) -> None:
    @app.exception_handler(HTTPException)
    async def http_exception_handler(
        request: Request,
        exc: HTTPException,
    ):
        logger.warning(
            "%s %s -> %s",
            request.method,
            request.url.path,
            exc.status_code,
        )

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "detail": exc.detail,
            },
        )

    @app.exception_handler(
        GitHubNotFoundError,
    )
    async def github_not_found_handler(
        request: Request,
        exc: GitHubNotFoundError,
    ):
        logger.warning(
            "%s %s -> 404 (%s)",
            request.method,
            request.url.path,
            exc,
        )

        return JSONResponse(
            status_code=404,
            content={
                "detail": str(exc),
            },
        )

    @app.exception_handler(
        RepositoryNotFoundError,
    )
    async def repository_not_found_handler(
        request: Request,
        exc: RepositoryNotFoundError,
    ):
        logger.warning(
            "%s %s -> 404 (%s)",
            request.method,
            request.url.path,
            exc,
        )

        return JSONResponse(
            status_code=404,
            content={
                "detail": str(exc),
            },
        )

    @app.exception_handler(
        GitHubAuthenticationError,
    )
    async def github_authentication_handler(
        request: Request,
        exc: GitHubAuthenticationError,
    ):
        logger.error(
            "%s %s -> GitHub authentication failed",
            request.method,
            request.url.path,
        )

        return JSONResponse(
            status_code=502,
            content={
                "detail": "GitHub authentication failed. Check the server GitHub credentials.",
            },
        )

    @app.exception_handler(
        GitHubRateLimitError,
    )
    async def github_rate_limit_handler(
        request: Request,
        exc: GitHubRateLimitError,
    ):
        logger.warning(
            "%s %s -> GitHub rate limit exceeded",
            request.method,
            request.url.path,
        )

        return JSONResponse(
            status_code=429,
            content={
                "detail": "GitHub API rate limit exceeded. Please try again later.",
            },
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(
        request: Request,
        exc: Exception,
    ):
        logger.exception(
            "Unhandled exception while processing %s %s",
            request.method,
            request.url.path,
        )

        return JSONResponse(
            status_code=500,
            content={
                "detail": "Internal server error",
            },
        )
