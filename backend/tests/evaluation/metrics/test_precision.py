from issuescout.evaluation.comparison.result import ComparisonResult
from issuescout.evaluation.metrics.precision import PrecisionMetric


def test_precision_empty():
    assert PrecisionMetric().compute([]) == 0.0


def test_precision():
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

    assert PrecisionMetric().compute(comparisons) == 0.5
