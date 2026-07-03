from issuescout.models.analysis import RelationPrediction
from issuescout.models.pull_request import PullRequest
from issuescout.ranking import Ranker


def test_single_prediction():
    ranker = Ranker()

    prediction = RelationPrediction(
        pull_request=PullRequest(
            number=1,
            title="PR",
            body="",
            branch_name="branch",
            author="alice",
        ),
        score=99,
        results=[],
    )

    ranked = ranker.rank(
        [
            prediction,
        ]
    )

    assert ranked == [prediction]
