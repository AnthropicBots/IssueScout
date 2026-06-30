from issuescout.evaluation.comparison.result import ComparisonResult
from issuescout.evaluation.metrics.summary import EvaluationSummaryMetric


def test_summary():

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
        )
    ]

    summary = EvaluationSummaryMetric().compute(
        comparisons,
    )

    assert summary.issue_count == 1
    assert summary.accuracy == 1.0
    assert summary.precision == 1.0
    assert summary.recall == 1.0
    assert summary.mrr == 1.0
    assert summary.map == 1.0
