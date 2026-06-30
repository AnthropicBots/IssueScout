from __future__ import annotations

import os


class GitHubAuthentication:
    """
    Helper for retrieving the GitHub personal access token.
    """

    ENVIRONMENT_VARIABLE = "GITHUB_TOKEN"

    @classmethod
    def token(cls) -> str | None:
        return os.getenv(cls.ENVIRONMENT_VARIABLE)

    @classmethod
    def configured(cls) -> bool:
        return cls.token() is not None
