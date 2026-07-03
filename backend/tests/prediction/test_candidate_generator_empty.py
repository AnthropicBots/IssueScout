from issuescout.models import Issue
from issuescout.prediction.candidate_generator import CandidateGenerator


def test_generate_with_no_pull_requests():
    generator = CandidateGenerator()

    issue = Issue(
        number=1,
        title="Bug",
        author="alice",
    )

    assert (
        generator.generate(
            issue,
            [],
        )
        == []
    )
