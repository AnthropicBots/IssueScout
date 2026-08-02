from datetime import UTC, datetime

from issuescout.models import Issue, PullRequest
from issuescout.prediction.candidate_generator import CandidateGenerator


def test_missing_issue_date_does_not_filter():
    generator = CandidateGenerator()

    issue = Issue(
        number=1,
        title="Bug",
        author="alice",
    )

    pr = PullRequest(
        number=10,
        title="Bug",
        body="",
        branch_name="feature",
        author="bob",
        created_at=datetime(
            2024,
            5,
            1,
            tzinfo=UTC,
        ),
    )

    assert generator._within_candidate_window(issue, pr)


def test_missing_pr_date_does_not_filter():
    generator = CandidateGenerator()

    issue = Issue(
        number=1,
        title="Bug",
        author="alice",
        created_at=datetime(
            2024,
            1,
            1,
            tzinfo=UTC,
        ),
    )

    pr = PullRequest(
        number=10,
        title="Bug",
        body="",
        branch_name="feature",
        author="bob",
    )

    assert generator._within_candidate_window(issue, pr)


def test_pr_before_issue_is_rejected():
    generator = CandidateGenerator()

    issue = Issue(
        number=1,
        title="Bug",
        author="alice",
        created_at=datetime(
            2024,
            2,
            1,
            tzinfo=UTC,
        ),
    )

    pr = PullRequest(
        number=10,
        title="Bug",
        body="",
        branch_name="feature",
        author="bob",
        created_at=datetime(
            2024,
            1,
            1,
            tzinfo=UTC,
        ),
    )

    assert not generator._within_candidate_window(issue, pr)
