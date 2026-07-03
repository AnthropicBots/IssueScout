from issuescout.scanner.builders.pull_request_builder import (
    PullRequestBuilder,
)


def test_builder_defaults():
    pull_request = {
        "number": 1,
        "title": "Fix bug",
        "body": None,
        "user": {"login": "alice"},
        "head": {"ref": "main"},
        "state": "open",
        "draft": False,
        "created_at": None,
        "updated_at": None,
        "closed_at": None,
        "merged_at": None,
        "labels": [],
    }

    result = PullRequestBuilder().build(
        pull_request,
        reviewers={"users": []},
        commits=[],
        branch_commit_history=[],
        changed_files=set(),
    )

    assert result.number == 1
    assert result.body == ""
    assert result.author == "alice"
    assert result.branch_name == "main"
    assert result.state == "open"
    assert result.draft is False
