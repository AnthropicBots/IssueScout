from issuescout.scanner.builders.pull_request_builder import (
    PullRequestBuilder,
)


def test_builder_commit_messages():
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

    commits = [
        {"commit": {"message": "First commit"}},
        {"commit": {"message": "Second commit"}},
    ]

    result = PullRequestBuilder().build(
        pull_request,
        reviewers={"users": []},
        commits=commits,
        branch_commit_history=[],
        changed_files=set(),
    )

    assert result.commit_messages == [
        "First commit",
        "Second commit",
    ]
