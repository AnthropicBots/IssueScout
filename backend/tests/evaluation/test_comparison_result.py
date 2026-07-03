from issuescout.evaluation.comparison.result import ComparisonResult


def test_top1_and_topk():
    result = ComparisonResult(
        repository_owner="owner",
        repository_name="repo",
        issue_number=1,
        actual_pull_request=10,
        predicted_pull_request=10,
        matched=True,
        rank=1,
        prediction_count=3,
        confidence=95.0,
    )

    assert result.top1 is True
    assert result.within_top_k(1) is True
    assert result.within_top_k(3) is True
