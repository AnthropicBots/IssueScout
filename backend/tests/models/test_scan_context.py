from issuescout.models.issue import Issue
from issuescout.models.pull_request import PullRequest
from issuescout.models.repository import Repository
from issuescout.models.scan_context import RepositoryScanContext


def test_scan_context_defaults():
    context = RepositoryScanContext(
        repository=Repository(
            owner="owner",
            name="repo",
        ),
    )

    assert context.issues == []
    assert context.pull_requests == []
    assert context.linked_pr_cache == {}


def test_scan_context_with_data():
    context = RepositoryScanContext(
        repository=Repository(
            owner="owner",
            name="repo",
        ),
        issues=[
            Issue(
                number=1,
                title="Issue",
                author="alice",
            )
        ],
        pull_requests=[
            PullRequest(
                number=2,
                title="PR",
                body="",
                branch_name="main",
                author="bob",
            )
        ],
    )

    assert len(context.issues) == 1
    assert len(context.pull_requests) == 1
