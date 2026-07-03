from issuescout.models.analysis import RelationPrediction
from issuescout.models.pull_request import PullRequest
from issuescout.ranking import Ranker


def prediction(score: int):
    return RelationPrediction(
        pull_request=PullRequest(
            number=score,
            title="PR",
            body="",
            branch_name="main",
            author="alice",
        ),
        score=score,
        results=[],
    )


def test_ranker_returns_all_predictions():
    ranker = Ranker()

    ranked = ranker.rank(
        [
            prediction(5),
            prediction(40),
            prediction(80),
        ]
    )

    assert len(ranked) == 3
    assert ranked[0].score >= ranked[-1].score
