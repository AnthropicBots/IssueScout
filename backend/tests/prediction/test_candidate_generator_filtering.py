from datetime import datetime

from issuescout.models import Issue, PullRequest
from issuescout.prediction.candidate_generator import CandidateGenerator


def test_filters_pr_outside_candidate_window():
    generator = CandidateGenerator()

    issue = Issue(
        number=1,
        title="Login bug",
        author="alice",
        created_at=datetime(2024, 1, 1),
    )

    pr = PullRequest(
        number=10,
        title="Login bug fix",
        body="",
        branch_name="fix-login",
        author="alice",
        created_at=datetime(2024, 6, 1),
    )

    candidates = generator.generate(
        issue,
        [pr],
    )

    assert candidates == []
