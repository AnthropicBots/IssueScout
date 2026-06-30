from issuescout.evaluation.models import (
    EvaluationRecord,
    GroundTruthRecord,
    PredictionCandidate,
)
from issuescout.evaluation.runner import EvaluationRunner


def test_runner_returns_single_result():
    runner = EvaluationRunner()

    record = EvaluationRecord(
        ground_truth=GroundTruthRecord(
            repository_owner="python",
            repository_name="cpython",
            issue_number=100,
            issue_title="Example issue",
            issue_state="closed",
            actual_pull_request=200,
        ),
        predictions=[
            PredictionCandidate(
                pull_request_number=200,
                score=0.95,
                confidence="high",
                rank=1,
            )
        ],
    )

    results = runner.run([record])

    assert len(results) == 1
    assert results[0].matched is True
    assert results[0].rank == 1
