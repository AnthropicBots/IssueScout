from __future__ import annotations

from issuescout.evaluation.comparison.result import ComparisonResult
from issuescout.evaluation.models import (
    EvaluationRecord,
)


class EvaluationComparator:
    """
    Compares IssueScout predictions against ground-truth data.
    """

    def compare(
        self,
        record: EvaluationRecord,
    ) -> ComparisonResult:

        actual = record.ground_truth.actual_pull_request

        for prediction in record.predictions:
            if prediction.pull_request_number == actual:
                return ComparisonResult(
                    repository_owner=record.ground_truth.repository_owner,
                    repository_name=record.ground_truth.repository_name,
                    issue_number=record.ground_truth.issue_number,
                    actual_pull_request=actual,
                    predicted_pull_request=prediction.pull_request_number,
                    matched=True,
                    rank=prediction.rank,
                    prediction_count=len(record.predictions),
                    confidence=prediction.score,
                )

        return ComparisonResult(
            repository_owner=record.ground_truth.repository_owner,
            repository_name=record.ground_truth.repository_name,
            issue_number=record.ground_truth.issue_number,
            actual_pull_request=actual,
            predicted_pull_request=None,
            matched=False,
            rank=None,
            prediction_count=len(record.predictions),
            confidence=0.0,
        )
