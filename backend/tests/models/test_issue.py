from issuescout.models.issue import Issue


def test_issue_defaults():
    issue = Issue(
        number=1,
        title="Bug",
        author="alice",
    )

    assert issue.assigned is False
    assert issue.state == "open"
    assert issue.labels == set()
    assert issue.timeline_pull_requests == set()
    assert issue.comment_pull_requests == set()


def test_issue_custom_fields():
    issue = Issue(
        number=10,
        title="Feature",
        author="bob",
        assigned=True,
        assignee="john",
        labels={"bug", "good first issue"},
    )

    assert issue.assignee == "john"
    assert "bug" in issue.labels
