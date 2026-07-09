from __future__ import annotations

from pydantic import BaseModel


class GitHubReference(BaseModel):
    """
    A GitHub reference discovered while analyzing
    repository data.
    """

    kind: str

    number: int | None = None

    sha: str | None = None

    repository: str | None = None

    source: str

    text: str

    confidence: float = 1.0
