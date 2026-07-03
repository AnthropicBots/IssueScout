from issuescout.scanner.builders.pull_request_builder import (
    PullRequestBuilder,
)


def test_builder_labels():
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
        "labels": [
            {"name": "bug"},
            {"name": "good first issue"},
        ],
    }

    result = PullRequestBuilder().build(
        pull_request,
        reviewers={"users": []},
        commits=[],
        branch_commit_history=[],
        changed_files=set(),
    )

    assert result.labels == {
        "bug",
        "good first issue",
    }
