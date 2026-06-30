from issuescout.evaluation.comparison.result import ComparisonResult
from issuescout.evaluation.metrics.recall import RecallMetric


def test_recall():
    comparisons = [
        ComparisonResult(
            repository_owner="python",
            repository_name="cpython",
            issue_number=1,
            actual_pull_request=10,
            predicted_pull_request=10,
            matched=True,
            rank=1,
            prediction_count=1,
            confidence=1.0,
        ),
        ComparisonResult(
            repository_owner="python",
            repository_name="cpython",
            issue_number=2,
            actual_pull_request=20,
            predicted_pull_request=None,
            matched=False,
            rank=None,
            prediction_count=1,
            confidence=0.0,
        ),
    ]

    assert RecallMetric().compute(comparisons) == 0.5
