from datetime import datetime

from pydantic import BaseModel, Field


class Issue(BaseModel):
    number: int

    title: str

    author: str

    assignee: str | None = None

    assigned: bool = False

    state: str = "open"

    created_at: datetime | None = None

    updated_at: datetime | None = None

    closed_at: datetime | None = None

    milestone: str | None = None

    timeline_pull_requests: set[int] = Field(
        default_factory=set,
    )

    comment_pull_requests: set[int] = Field(
        default_factory=set,
    )

    body_pull_requests: set[int] = Field(
        default_factory=set,
    )

    commit_pull_requests: set[int] = Field(
        default_factory=set,
    )

    body: str | None = None

    comments: list[dict] = Field(
        default_factory=list,
    )

    timeline_events: list[dict] = Field(
        default_factory=list,
    )

    mentioned_files: set[str] = Field(
        default_factory=set,
    )

    labels: set[str] = Field(
        default_factory=set,
    )
