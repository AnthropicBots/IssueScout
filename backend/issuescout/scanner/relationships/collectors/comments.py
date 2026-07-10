from __future__ import annotations

from issuescout.models.relationships import (
    Relationship,
    RelationshipSource,
)
from issuescout.scanner.relationships.parsers import (
    GitHubRelationshipParser,
)


class CommentRelationshipCollector:
    """
    Collects relationships from issue comments.
    """

    def __init__(self) -> None:
        self._parser = GitHubRelationshipParser()

    def collect(
        self,
        comments: list[dict],
    ) -> list[Relationship]:

        relationships: list[Relationship] = []

        for comment in comments:
            relationships.extend(
                self._parser.parse(
                    comment.get("body") or "",
                    source=RelationshipSource.ISSUE_COMMENT,
                )
            )

        return relationships
