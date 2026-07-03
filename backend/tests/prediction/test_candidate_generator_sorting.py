from datetime import datetime

from issuescout.models import Issue, PullRequest
from issuescout.prediction.candidate_generator import CandidateGenerator


def test_returns_matching_candidates():
    generator = CandidateGenerator()

    issue = Issue(
        number=42,
        title="Crash on startup",
        author="alice",
        created_at=datetime(2024, 1, 1),
    )

    matching = PullRequest(
        number=1,
        title="Startup crash fix",
        body="",
        branch_name="fix-startup",
        author="alice",
        created_at=datetime(2024, 1, 2),
    )

    non_matching = PullRequest(
        number=2,
        title="Update docs",
        body="",
        branch_name="docs",
        author="bob",
        created_at=datetime(2024, 1, 2),
    )

    candidates = generator.generate(
        issue,
        [
            matching,
            non_matching,
        ],
    )

    assert candidates == [matching]
