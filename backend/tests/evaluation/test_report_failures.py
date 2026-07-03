from issuescout.evaluation.report import EvaluationFailure


def test_failure_defaults():
    failure = EvaluationFailure(
        issue_number=1,
        actual_pull_request=10,
        predicted_pull_request=20,
        predicted_rank=1,
        prediction_score=95.5,
    )

    assert failure.issue_number == 1
    assert failure.reason == ""
