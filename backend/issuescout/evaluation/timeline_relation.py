from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class TimelineEvidence:
    """
    Represents one piece of evidence extracted from a GitHub issue timeline.

    A single issue timeline may contain multiple independent pieces of
    evidence that relate an issue to one or more pull requests.
    """

    event_type: str

    source: str

    pull_request_number: int | None

    confidence: float

    metadata: dict[str, str] = field(default_factory=dict)


@dataclass(slots=True)
class TimelineRelation:
    """
    Final resolved relationship extracted from an issue timeline.

    The resolver combines multiple TimelineEvidence objects into one
    canonical relation used throughout IssueScout.
    """

    pull_request_number: int | None

    confidence: float

    evidence: list[TimelineEvidence] = field(default_factory=list)

    merged: bool = False

    closed_issue: bool = False

    linkage_method: str = "unknown"

    metadata: dict[str, str] = field(default_factory=dict)

    @property
    def resolved(self) -> bool:
        """
        Returns True if a pull request could be resolved.
        """
        return self.pull_request_number is not None
