from issuescout.models.pull_request import PullRequest


def test_pull_request_defaults():
    pr = PullRequest(
        number=5,
        title="Fix bug",
        body="body",
        branch_name="fix-5",
        author="alice",
    )

    assert pr.state == "open"
    assert pr.draft is False
    assert pr.labels == set()
    assert pr.related_issues == set()
    assert pr.reviewers == set()


def test_pull_request_custom_values():
    pr = PullRequest(
        number=20,
        title="Feature",
        body="text",
        branch_name="feature",
        author="bob",
        labels={"enhancement"},
        related_issues={12},
    )

    assert 12 in pr.related_issues
    assert "enhancement" in pr.labels
