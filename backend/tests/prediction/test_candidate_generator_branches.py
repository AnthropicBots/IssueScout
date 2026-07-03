from datetime import datetime

from issuescout.models import Issue, PullRequest
from issuescout.prediction.candidate_generator import CandidateGenerator


def test_related_issue_is_candidate():
    generator = CandidateGenerator()

    issue = Issue(
        number=42,
        title="Bug",
        author="alice",
        created_at=datetime(2024, 1, 1),
    )

    pr = PullRequest(
        number=10,
        title="Something",
        body="",
        branch_name="feature",
        author="bob",
        created_at=datetime(2024, 1, 2),
        related_issues={42},
    )

    assert generator.generate(issue, [pr]) == [pr]


def test_shared_labels_make_candidate():
    generator = CandidateGenerator()

    issue = Issue(
        number=1,
        title="Bug",
        author="alice",
        labels={"bug"},
        created_at=datetime(2024, 1, 1),
    )

    pr = PullRequest(
        number=5,
        title="Random",
        body="",
        branch_name="branch",
        author="bob",
        created_at=datetime(2024, 1, 2),
        labels={"bug"},
    )

    assert generator.generate(issue, [pr]) == [pr]
