from __future__ import annotations

from issuescout.evaluation.comparison.comparator import EvaluationComparator
from issuescout.evaluation.comparison.result import ComparisonResult
from issuescout.evaluation.metrics.accuracy import AccuracyMetric
from issuescout.evaluation.metrics.summary import EvaluationSummary


class EvaluationPipeline:
    """
    High-level orchestration for IssueScout evaluation.

    The pipeline coordinates the comparison stage and the metric
    computation stage while keeping both independent.

    Workflow

        Predictions
              │
              ▼
        Comparator
              │
              ▼
      Comparison Results
              │
              ▼
      Evaluation Metrics
              │
              ▼
      Evaluation Summary
    """

    def __init__(self) -> None:
        self.comparator = EvaluationComparator()
        self.accuracy_metric = AccuracyMetric()

    def summarize(
        self,
        comparisons: list[ComparisonResult],
    ) -> EvaluationSummary:
        """
        Compute evaluation metrics for a collection of comparison results.
        """

        accuracy = self.accuracy_metric.compute(
            comparisons,
        )

        return EvaluationSummary(
            issue_count=len(comparisons),
            accuracy=accuracy,
        )
