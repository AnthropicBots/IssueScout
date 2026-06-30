from __future__ import annotations

from issuescout.evaluation.comparison.result import ComparisonResult


class MeanAveragePrecision:
    """
    Computes Mean Average Precision (MAP).

    Since IssueScout predicts a single correct pull request for each issue,
    AP is equivalent to 1/rank when a correct prediction exists.
    """

    def compute(
        self,
        results: list[ComparisonResult],
    ) -> float:

        if not results:
            return 0.0

        total = 0.0

        for result in results:
            if result.matched and result.rank is not None:
                total += 1 / result.rank

        return total / len(results)


# Backward-compatible alias
MeanAveragePrecisionMetric = MeanAveragePrecision
