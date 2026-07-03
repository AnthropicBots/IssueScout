from issuescout.scanner.builders.pull_request_builder import (
    PullRequestBuilder,
)


def test_builder_reviewers():
    pull_request = {
        "number": 2,
        "title": "PR",
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

    result = PullRequestBuilder().build(
        pull_request,
        reviewers={
            "users": [
                {"login": "bob"},
                {"login": "charlie"},
            ]
        },
        commits=[],
        branch_commit_history=[],
        changed_files=set(),
    )

    assert result.reviewers == {
        "bob",
        "charlie",
    }
