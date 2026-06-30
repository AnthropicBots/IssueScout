from issuescout.evaluation.comparison.result import ComparisonResult
from issuescout.evaluation.metrics.map import MeanAveragePrecision


def test_map():

    metric = MeanAveragePrecision()

    results = [
        ComparisonResult(
            repository_owner="python",
            repository_name="cpython",
            issue_number=1,
            actual_pull_request=10,
            predicted_pull_request=10,
            matched=True,
            rank=1,
            prediction_count=5,
            confidence=0.9,
        ),
        ComparisonResult(
            repository_owner="python",
            repository_name="cpython",
            issue_number=2,
            actual_pull_request=20,
            predicted_pull_request=21,
            matched=False,
            rank=None,
            prediction_count=5,
            confidence=0.0,
        ),
    ]

    assert metric.compute(results) == 0.5
