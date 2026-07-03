from issuescout.evaluation.comparison.comparator import EvaluationComparator
from issuescout.evaluation.models import (
    EvaluationRecord,
    GroundTruthRecord,
)


def test_compare_without_predictions():
    record = EvaluationRecord(
        ground_truth=GroundTruthRecord(
            repository_owner="owner",
            repository_name="repo",
            issue_number=1,
            issue_title="Issue",
            issue_state="closed",
            actual_pull_request=100,
        ),
        predictions=[],
    )

    result = EvaluationComparator().compare(record)

    assert result.prediction_count == 0
    assert result.matched is False
