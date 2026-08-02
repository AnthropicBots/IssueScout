from datetime import UTC, datetime

from issuescout.models import Issue, PullRequest
from issuescout.prediction.candidate_generator import CandidateGenerator


def test_branch_name_matching_issue_number():
    generator = CandidateGenerator()

    issue = Issue(
        number=123,
        title="Improve docs",
        author="alice",
        created_at=datetime(
            2024,
            1,
            1,
            tzinfo=UTC,
        ),
    )

    pr = PullRequest(
        number=55,
        title="Completely different title",
        body="",
        branch_name="feature/123-docs",
        author="bob",
        created_at=datetime(
            2024,
            1,
            2,
            tzinfo=UTC,
        ),
    )

    candidates = generator.generate(
        issue,
        [pr],
    )

    assert candidates == [pr]
