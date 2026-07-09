from __future__ import annotations

from pydantic import BaseModel


class ResolvedReference(BaseModel):
    """
    A GitHub reference that has been resolved
    against the GitHub API.
    """

    number: int

    kind: str

    exists: bool

    title: str | None = None

    state: str | None = None

    merged: bool | None = None

    url: str | None = None
