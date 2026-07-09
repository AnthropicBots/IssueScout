from __future__ import annotations

from pydantic import BaseModel, Field


class IssueIntelligence(BaseModel):
    """
    Aggregated intelligence collected for a GitHub issue.
    """

    number: int

    title: str

    body: str = ""

    labels: set[str] = Field(default_factory=set)

    participants: set[str] = Field(default_factory=set)

    mentioned_pull_requests: set[int] = Field(
        default_factory=set,
    )

    mentioned_issues: set[int] = Field(
        default_factory=set,
    )

    mentioned_commits: set[str] = Field(
        default_factory=set,
    )

    comments: list[str] = Field(
        default_factory=list,
    )

    timeline_events: list[dict] = Field(
        default_factory=list,
    )
