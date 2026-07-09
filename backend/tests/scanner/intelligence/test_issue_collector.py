import pytest

from issuescout.scanner.intelligence.issue.collector import (
    IssueIntelligenceCollector,
)

from tests.helpers.factories import make_issue


@pytest.mark.anyio
async def test_collect_builds_issue_intelligence():
    issue = make_issue(
        title="Issue #10",
        body="Fixed by #20",
    )

    collector = IssueIntelligenceCollector()

    intelligence = await collector.collect(issue)

    assert intelligence.issue_number == issue.number
    assert intelligence.title == issue.title
    assert intelligence.author == issue.author
    assert intelligence.mentioned_pull_request_numbers == {10, 20}


@pytest.mark.anyio
async def test_collect_with_comments():
    issue = make_issue()

    collector = IssueIntelligenceCollector()

    intelligence = await collector.collect(
        issue,
        comments=[
            {
                "body": "See #44",
            }
        ],
    )

    assert intelligence.comments is not None
    assert 44 in issue.comment_pull_requests
