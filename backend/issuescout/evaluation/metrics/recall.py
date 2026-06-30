from __future__ import annotations

from issuescout.evaluation.comparison.result import ComparisonResult


class RecallMetric:
    """
    Computes recall for IssueScout predictions.

    Since each evaluation record contains exactly one ground-truth pull
    request, recall is the fraction of issues for which the correct pull
    request was successfully predicted.
    """

    def compute(
        self,
        comparisons: list[ComparisonResult],
    ) -> float:

        if not comparisons:
            return 0.0

        recovered = sum(comparison.matched for comparison in comparisons)

        return recovered / len(comparisons)
