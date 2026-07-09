from issuescout.scanner.relationship import (
    RelationshipScorer,
)

from tests.helpers.factories import (
    make_issue,
    make_pull_request,
)


def test_score_with_no_relationships():

    scorer = RelationshipScorer()

    score = scorer.score(
        make_issue(),
        make_pull_request(),
    )

    assert score == 0


def test_body_reference_scores():

    issue = make_issue(
        body_pull_requests={10},
    )

    scorer = RelationshipScorer()

    assert (
        scorer.score(
            issue,
            make_pull_request(
                number=10,
            ),
        )
        == 3
    )


def test_comment_reference_scores():

    issue = make_issue(
        comment_pull_requests={10},
    )

    scorer = RelationshipScorer()

    assert (
        scorer.score(
            issue,
            make_pull_request(
                number=10,
            ),
        )
        == 3
    )


def test_timeline_reference_scores():

    issue = make_issue(
        timeline_pull_requests={10},
    )

    scorer = RelationshipScorer()

    assert (
        scorer.score(
            issue,
            make_pull_request(
                number=10,
            ),
        )
        == 5
    )


def test_commit_reference_scores():

    issue = make_issue(
        commit_pull_requests={10},
    )

    scorer = RelationshipScorer()

    assert (
        scorer.score(
            issue,
            make_pull_request(
                number=10,
            ),
        )
        == 4
    )


def test_file_overlap_scores():

    issue = make_issue(
        mentioned_files={
            "app.py",
        },
    )

    pr = make_pull_request(
        changed_files={
            "app.py",
        },
    )

    scorer = RelationshipScorer()

    assert (
        scorer.score(
            issue,
            pr,
        )
        == 2
    )


def test_combined_score():

    issue = make_issue(
        body_pull_requests={10},
        comment_pull_requests={10},
        timeline_pull_requests={10},
        commit_pull_requests={10},
        mentioned_files={
            "app.py",
        },
    )

    pr = make_pull_request(
        number=10,
        changed_files={
            "app.py",
        },
    )

    scorer = RelationshipScorer()

    assert (
        scorer.score(
            issue,
            pr,
        )
        == 17
    )
