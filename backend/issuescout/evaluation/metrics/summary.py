from __future__ import annotations

from dataclasses import dataclass

from issuescout.evaluation.comparison.result import ComparisonResult
from issuescout.evaluation.metrics.accuracy import AccuracyMetric
from issuescout.evaluation.metrics.map import MeanAveragePrecisionMetric
from issuescout.evaluation.metrics.mrr import MeanReciprocalRankMetric
from issuescout.evaluation.metrics.precision import PrecisionMetric
from issuescout.evaluation.metrics.recall import RecallMetric


@dataclass(slots=True)
class EvaluationSummary:
    """
    Overall benchmark statistics.
    """

    issue_count: int

    accuracy: float

    precision: float

    recall: float

    mrr: float

    map: float

    def to_dict(self) -> dict:
        """
        Convert the evaluation summary into a serializable dictionary.
        """

        return {
            "issue_count": self.issue_count,
            "accuracy": self.accuracy,
            "precision": self.precision,
            "recall": self.recall,
            "mrr": self.mrr,
            "map": self.map,
        }


class EvaluationSummaryMetric:
    """
    Computes all evaluation metrics together and returns a single summary.
    """

    def compute(
        self,
        comparisons: list[ComparisonResult],
    ) -> EvaluationSummary:

        return EvaluationSummary(
            issue_count=len(comparisons),
            accuracy=AccuracyMetric().compute(comparisons),
            precision=PrecisionMetric().compute(comparisons),
            recall=RecallMetric().compute(comparisons),
            mrr=MeanReciprocalRankMetric().compute(comparisons),
            map=MeanAveragePrecisionMetric().compute(comparisons),
        )
