from datetime import datetime

from issuescout.models import Issue, PullRequest
from issuescout.prediction.candidate_generator import CandidateGenerator


def test_similar_titles_make_candidate():
    generator = CandidateGenerator()

    issue = Issue(
        number=1,
        title="Fix login page crash",
        author="alice",
        created_at=datetime(2024, 1, 1),
    )

    pr = PullRequest(
        number=99,
        title="Fix login page crash",
        body="",
        branch_name="feature",
        author="bob",
        created_at=datetime(2024, 1, 2),
    )

    assert generator.generate(issue, [pr]) == [pr]
