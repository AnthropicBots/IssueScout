from issuescout.models.analysis import RelationPrediction
from issuescout.models.pull_request import PullRequest
from issuescout.ranking import Ranker


def prediction(number: int, score: int):
    return RelationPrediction(
        pull_request=PullRequest(
            number=number,
            title="PR",
            body="",
            branch_name="main",
            author="alice",
        ),
        score=score,
        results=[],
    )


def test_ranker_sorts_descending():
    ranker = Ranker()

    ranked = ranker.rank(
        [
            prediction(1, 10),
            prediction(2, 50),
            prediction(3, 30),
        ]
    )

    assert [item.pull_request.number for item in ranked] == [
        2,
        3,
        1,
    ]
