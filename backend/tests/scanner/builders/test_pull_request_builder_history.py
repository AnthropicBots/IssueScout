from issuescout.scanner.builders.pull_request_builder import (
    PullRequestBuilder,
)


def test_builder_branch_history():
    pull_request = {
        "number": 1,
        "title": "Fix",
        "body": "",
        "user": {"login": "alice"},
        "head": {"ref": "feature"},
        "state": "open",
        "draft": False,
        "created_at": None,
        "updated_at": None,
        "closed_at": None,
        "merged_at": None,
        "labels": [],
    }

    history = [
        "abc123",
        "def456",
    ]

    result = PullRequestBuilder().build(
        pull_request,
        reviewers={"users": []},
        commits=[],
        branch_commit_history=history,
        changed_files={"a.py", "b.py"},
    )

    assert result.branch_commit_history == history
    assert result.changed_files == {
        "a.py",
        "b.py",
    }
