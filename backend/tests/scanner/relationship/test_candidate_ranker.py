from issuescout.scanner.ranking import (
    CandidateRanker,
)

from tests.helpers.factories import (
    make_issue,
    make_pull_request,
)


def test_rank_returns_same_number_of_candidates():

    ranker = CandidateRanker()

    issue = make_issue()

    candidates = [
        make_pull_request(number=1),
        make_pull_request(number=2),
    ]

    ranked = ranker.rank(
        issue,
        candidates,
    )

    assert len(ranked) == 2


def test_stronger_relationship_ranks_first():

    issue = make_issue(
        timeline_pull_requests={2},
    )

    ranker = CandidateRanker()

    ranked = ranker.rank(
        issue,
        [
            make_pull_request(number=1),
            make_pull_request(number=2),
        ],
    )

    assert ranked[0].number == 2


def test_empty_candidate_list():

    ranker = CandidateRanker()

    assert (
        ranker.rank(
            make_issue(),
            [],
        )
        == []
    )


def test_multiple_relationships_beat_single_relationship():

    issue = make_issue(
        body_pull_requests={2},
        timeline_pull_requests={2},
    )

    ranker = CandidateRanker()

    ranked = ranker.rank(
        issue,
        [
            make_pull_request(number=1),
            make_pull_request(number=2),
        ],
    )

    assert ranked[0].number == 2
