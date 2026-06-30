from issuescout.evaluation.comparison.result import ComparisonResult
from issuescout.evaluation.metrics.accuracy import AccuracyMetric


def make_result(
    matched: bool,
) -> ComparisonResult:
    return ComparisonResult(
        repository_owner="python",
        repository_name="cpython",
        issue_number=1,
        actual_pull_request=100,
        predicted_pull_request=100 if matched else 200,
        matched=matched,
        rank=1 if matched else None,
        prediction_count=3,
        confidence=1.0 if matched else 0.0,
    )


def test_accuracy_all_correct():
    metric = AccuracyMetric()

    result = metric.compute(
        [
            make_result(True),
            make_result(True),
            make_result(True),
        ]
    )

    assert result == 1.0


def test_accuracy_half_correct():
    metric = AccuracyMetric()

    result = metric.compute(
        [
            make_result(True),
            make_result(False),
            make_result(True),
            make_result(False),
        ]
    )

    assert result == 0.5


def test_accuracy_none_correct():
    metric = AccuracyMetric()

    result = metric.compute(
        [
            make_result(False),
            make_result(False),
        ]
    )

    assert result == 0.0


def test_accuracy_empty():
    metric = AccuracyMetric()

    assert metric.compute([]) == 0.0
