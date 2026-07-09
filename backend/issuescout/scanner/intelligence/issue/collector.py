from __future__ import annotations

from issuescout.models import Issue
from issuescout.scanner.intelligence.issue.body_collector import (
    IssueBodyCollector,
)
from issuescout.scanner.intelligence.models import (
    IssueIntelligence,
)
from issuescout.scanner.resolver import (
    ReferenceResolver,
)
from issuescout.scanner.intelligence.issue.comment_collector import (
    IssueCommentCollector,
)


class IssueIntelligenceCollector:
    """
    Collects issue-level intelligence.

    Future iterations will enrich the collected
    information with comments, timeline events,
    discussions, and additional relationship
    evidence extracted from GitHub.
    """

    def __init__(self) -> None:
        self.reference_resolver = ReferenceResolver()
        self.body_collector = IssueBodyCollector()
        self.comment_collector = IssueCommentCollector()

    async def collect(
        self,
        issue: Issue,
        comments: list[dict] | None = None,
    ) -> IssueIntelligence:
        self.body_collector.collect(
            issue,
        )

        if comments:
            self.comment_collector.collect(
                issue,
                comments,
            )

        return IssueIntelligence(
            issue_number=issue.number,
            title=issue.title,
            body=issue.body,
            labels=sorted(issue.labels),
            author=issue.author,
            assignee=issue.assignee,
            milestone=issue.milestone,
            mentioned_issue_numbers=set(),
            mentioned_pull_request_numbers=set(
                issue.body_pull_requests,
            ),
            comments=comments,
        )
