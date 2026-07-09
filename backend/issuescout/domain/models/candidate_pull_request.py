from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(
    slots=True,
    frozen=True,
)
class CandidatePullRequest:
    """
    Represents a pull request that may resolve
    an issue.
    """

    number: int

    url: str

    sources: set[str] = field(
        default_factory=set,
    )
