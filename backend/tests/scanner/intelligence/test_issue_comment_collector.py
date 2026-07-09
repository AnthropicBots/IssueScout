from issuescout.scanner.intelligence.issue.comment_collector import (
    IssueCommentCollector,
)

from tests.helpers.factories import make_issue


def test_collect_comment_references():
    issue = make_issue()

    collector = IssueCommentCollector()

    collector.collect(
        issue,
        [
            {"body": "Solved in #12"},
            {"body": "See #15"},
        ],
    )

    assert issue.comment_pull_requests == {12, 15}


def test_collect_missing_comment_body():
    issue = make_issue()

    collector = IssueCommentCollector()

    collector.collect(
        issue,
        [
            {},
        ],
    )

    assert issue.comment_pull_requests == set()
