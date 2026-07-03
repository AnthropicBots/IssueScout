from issuescout.models.analysis import RelationPrediction
from issuescout.models.pull_request import PullRequest
from issuescout.ranking import Ranker


def prediction(number: int):
    return RelationPrediction(
        pull_request=PullRequest(
            number=number,
            title="PR",
            body="",
            branch_name="main",
            author="alice",
        ),
        score=50,
        results=[],
    )


def test_duplicate_scores_are_preserved():
    ranker = Ranker()

    ranked = ranker.rank(
        [
            prediction(1),
            prediction(2),
        ]
    )

    assert len(ranked) == 2
    assert ranked[0].score == ranked[1].score
