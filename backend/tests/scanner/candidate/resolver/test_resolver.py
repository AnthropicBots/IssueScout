from issuescout.models import PullRequest
from issuescout.scanner.candidate.resolver import (
    CandidateResolver,
)


def make_pr(
    number: int,
) -> PullRequest:

    return PullRequest(
        number=number,
        title=f"PR {number}",
        body="",
        state="open",
        author="octocat",
        branch_name=f"branch-{number}",
    )


def test_resolve_all_candidates():

    resolver = CandidateResolver()

    lookup = {
        1: make_pr(1),
        2: make_pr(2),
        3: make_pr(3),
    }

    resolved, missing = resolver.resolve(
        {1, 2, 3},
        lookup,
    )

    assert [pr.number for pr in resolved] == [
        1,
        2,
        3,
    ]

    assert missing == set()


def test_resolve_some_missing():

    resolver = CandidateResolver()

    lookup = {
        1: make_pr(1),
        3: make_pr(3),
    }

    resolved, missing = resolver.resolve(
        {1, 2, 3},
        lookup,
    )

    assert [pr.number for pr in resolved] == [
        1,
        3,
    ]

    assert missing == {2}


def test_resolve_all_missing():

    resolver = CandidateResolver()

    resolved, missing = resolver.resolve(
        {5, 6},
        {},
    )

    assert resolved == []

    assert missing == {
        5,
        6,
    }


def test_resolve_empty_candidates():

    resolver = CandidateResolver()

    resolved, missing = resolver.resolve(
        set(),
        {},
    )

    assert resolved == []

    assert missing == set()


def test_candidates_are_sorted():

    resolver = CandidateResolver()

    lookup = {
        1: make_pr(1),
        2: make_pr(2),
        3: make_pr(3),
    }

    resolved, _ = resolver.resolve(
        {3, 1, 2},
        lookup,
    )

    assert [pr.number for pr in resolved] == [
        1,
        2,
        3,
    ]
