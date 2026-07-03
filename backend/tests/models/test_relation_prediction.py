from issuescout.models.analysis import RelationPrediction
from issuescout.models.pull_request import PullRequest


def test_relation_prediction_defaults():
    prediction = RelationPrediction(
        pull_request=PullRequest(
            number=1,
            title="PR",
            body="",
            branch_name="main",
            author="alice",
        ),
        score=88,
        results=[],
    )

    assert prediction.score == 88
    assert prediction.results == []
    assert prediction.strong_evidence is False
