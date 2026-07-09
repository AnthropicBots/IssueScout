from __future__ import annotations

from issuescout.models import Issue
from issuescout.scanner.resolver import (
    ReferenceResolver,
)


class IssueTimelineReferenceCollector:
    """
    Extracts pull request references from
    GitHub timeline events.
    """

    def __init__(self) -> None:
        self.reference_resolver = ReferenceResolver()

    def collect(
        self,
        issue: Issue,
        timeline_events: list[dict],
    ) -> None:

        for event in timeline_events:
            body = ""

            source = event.get("source")

            if isinstance(source, dict):
                issue_data = source.get("issue")

                if isinstance(issue_data, dict):
                    body = issue_data.get("body") or ""

            issue.timeline_pull_requests.update(
                self.reference_resolver.resolve(
                    body,
                )
            )
