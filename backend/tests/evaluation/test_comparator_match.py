from issuescout.evaluation.comparison.comparator import EvaluationComparator
from issuescout.evaluation.models import (
    EvaluationRecord,
    GroundTruthRecord,
    PredictionCandidate,
)


def test_compare_match():
    record = EvaluationRecord(
        ground_truth=GroundTruthRecord(
            repository_owner="owner",
            repository_name="repo",
            issue_number=1,
            issue_title="Issue",
            issue_state="closed",
            actual_pull_request=100,
        ),
        predictions=[
            PredictionCandidate(
                pull_request_number=100,
                score=98.0,
                confidence="High",
                rank=1,
            ),
        ],
    )

    result = EvaluationComparator().compare(record)

    assert result.matched is True
    assert result.rank == 1
    assert result.predicted_pull_request == 100
