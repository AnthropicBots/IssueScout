from issuescout.scanner.intelligence.models import (
    IssueIntelligence,
    RepositoryIntelligence,
)


def test_repository_intelligence_model():

    model = RepositoryIntelligence(
        owner="python",
        name="cpython",
        description=None,
        homepage=None,
        language="Python",
        default_branch="main",
        license_name="PSF",
        stars=10,
        forks=2,
        watchers=1,
        open_issues=5,
        archived=False,
        disabled=False,
        topics=["python"],
    )

    assert model.owner == "python"
    assert model.topics == ["python"]


def test_issue_intelligence_model():

    model = IssueIntelligence(
        issue_number=10,
        title="Fix login",
        body="body",
        labels=["bug"],
        author="alice",
        assignee="bob",
        milestone="v1",
        mentioned_issue_numbers={1, 2},
        mentioned_pull_request_numbers={20},
        comments=[],
    )

    assert model.issue_number == 10
    assert model.author == "alice"
    assert model.mentioned_pull_request_numbers == {20}
