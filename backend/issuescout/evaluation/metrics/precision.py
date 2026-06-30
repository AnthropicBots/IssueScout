from __future__ import annotations

from issuescout.evaluation.comparison.result import ComparisonResult


class PrecisionMetric:
    """
    Computes precision for IssueScout predictions.

    Precision measures the fraction of predicted pull requests that are
    correct.

    Since IssueScout predicts one ranked result list per issue,
    precision is equivalent to the ratio of matched predictions.
    """

    def compute(
        self,
        comparisons: list[ComparisonResult],
    ) -> float:

        if not comparisons:
            return 0.0

        matched = sum(comparison.matched for comparison in comparisons)

        return matched / len(comparisons)
