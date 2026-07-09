from __future__ import annotations

from issuescout.models import Issue
from issuescout.scanner.resolver import (
    ReferenceResolver,
)


class IssueCommentCollector:
    """
    Extracts PR references from issue comments.
    """

    def __init__(self) -> None:
        self.reference_resolver = ReferenceResolver()

    def collect(
        self,
        issue: Issue,
        comments: list[dict],
    ) -> None:

        for comment in comments:
            issue.comment_pull_requests.update(
                self.reference_resolver.resolve(
                    comment.get(
                        "body",
                        "",
                    )
                )
            )
