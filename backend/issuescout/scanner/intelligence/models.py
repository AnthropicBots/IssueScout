from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class RepositoryIntelligence:
    """
    Repository-level intelligence collected before
    issue analysis begins.
    """

    owner: str
    name: str

    description: str | None

    homepage: str | None

    language: str | None

    default_branch: str

    license_name: str | None

    stars: int
    forks: int
    watchers: int

    open_issues: int

    archived: bool
    disabled: bool

    topics: list[str]


@dataclass(slots=True)
class IssueIntelligence:
    """
    Intelligence extracted from an individual issue.

    Initially, this model captures the raw textual
    information required for deeper relationship
    analysis. Future iterations will expand it with
    timeline events, discussion summaries, extracted
    references, and semantic metadata.
    """

    issue_number: int

    title: str

    body: str | None

    labels: list[str]

    author: str

    assignee: str | None

    milestone: str | None

    mentioned_issue_numbers: set[int]

    mentioned_pull_request_numbers: set[int]

    comments: list[dict] | None = None
