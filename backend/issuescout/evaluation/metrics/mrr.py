from __future__ import annotations

from issuescout.evaluation.comparison.result import ComparisonResult


class MeanReciprocalRank:
    """
    Computes Mean Reciprocal Rank (MRR).
    """

    def compute(
        self,
        results: list[ComparisonResult],
    ) -> float:

        if not results:
            return 0.0

        reciprocal = 0.0

        for result in results:
            if result.matched and result.rank is not None:
                reciprocal += 1 / result.rank

        return reciprocal / len(results)


# Backward-compatible alias
MeanReciprocalRankMetric = MeanReciprocalRank
