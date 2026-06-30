from __future__ import annotations

from issuescout.evaluation.comparison.result import ComparisonResult


class AccuracyMetric:
    """
    Computes Accuracy@K for IssueScout predictions.

    Accuracy@K answers:

        "For how many issues was the correct pull request found
        within the first K predictions?"

    Example

        8 correct out of 10 issues

        Accuracy = 0.80
    """

    def compute(
        self,
        comparisons: list[ComparisonResult],
    ) -> float:
        """
        Compute Accuracy.

        Returns a value between 0 and 1.
        """

        if not comparisons:
            return 0.0

        correct = sum(comparison.matched for comparison in comparisons)

        return correct / len(comparisons)
