from __future__ import annotations

from issuescout.models import Issue
from issuescout.scanner.resolver import (
    ReferenceResolver,
)


class IssueBodyCollector:
    """
    Extracts relationship evidence from an
    issue's title and description.
    """

    def __init__(self) -> None:
        self.reference_resolver = ReferenceResolver()

    def collect(
        self,
        issue: Issue,
    ) -> None:
        text = "\n".join(
            filter(
                None,
                [
                    issue.title,
                    issue.body,
                ],
            )
        )

        issue.body_pull_requests.update(
            self.reference_resolver.resolve(
                text,
            )
        )
