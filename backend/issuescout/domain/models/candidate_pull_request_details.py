from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class CandidatePullRequestDetails:
    """
    Complete information about a candidate
    pull request.
    """

    number: int

    title: str

    body: str

    state: str

    merged: bool

    author: str

    labels: set[str] = field(
        default_factory=set,
    )

    changed_files: set[str] = field(
        default_factory=set,
    )

    commits: list[str] = field(
        default_factory=list,
    )

    review_count: int = 0

    comment_count: int = 0

    discussion_keywords: list[str] = field(
        default_factory=list,
    )

    discussion_confidence: int = 0
