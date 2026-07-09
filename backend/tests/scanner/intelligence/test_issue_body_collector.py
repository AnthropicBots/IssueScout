from issuescout.scanner.intelligence.issue.body_collector import (
    IssueBodyCollector,
)

from tests.helpers.factories import make_issue


def test_collect_from_title_and_body():
    issue = make_issue(
        title="Fix bug #10",
        body="Duplicate of #20",
    )

    collector = IssueBodyCollector()

    collector.collect(issue)

    assert issue.body_pull_requests == {10, 20}


def test_collect_with_empty_text():
    issue = make_issue(
        title="",
        body="",
    )

    collector = IssueBodyCollector()

    collector.collect(issue)

    assert issue.body_pull_requests == set()
