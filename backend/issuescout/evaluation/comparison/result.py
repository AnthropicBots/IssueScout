from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ComparisonResult:
    """
    Represents the comparison between one ground-truth record and one
    prediction produced by IssueScout.

    This object is the canonical input for all evaluation metrics.
    """

    repository_owner: str

    repository_name: str

    issue_number: int

    actual_pull_request: int | None

    predicted_pull_request: int | None

    matched: bool

    rank: int | None

    prediction_count: int

    confidence: float

    @property
    def top1(self) -> bool:
        """
        True if the correct pull request was ranked first.
        """
        return self.rank == 1

    def within_top_k(
        self,
        k: int,
    ) -> bool:
        """
        Returns True if the correct pull request appears within Top-K.
        """

        return self.rank is not None and self.rank <= k
