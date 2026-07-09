from __future__ import annotations

from issuescout.models import Issue


class IssueEnricher:
    """
    Lazily enriches an issue with additional
    intelligence such as comments, timeline
    events, and discussion metadata.

    Expensive GitHub API requests are only
    performed when an analyzer actually
    requires them.
    """

    async def enrich(
        self,
        issue: Issue,
    ) -> Issue:
        return issue
