from __future__ import annotations

from issuescout.models.relationships import (
    Relationship,
    RelationshipSource,
)
from issuescout.scanner.relationships.parsers import (
    GitHubRelationshipParser,
)


class BodyRelationshipCollector:
    """
    Collects relationships from issue or pull request bodies.
    """

    def __init__(self) -> None:
        self._parser = GitHubRelationshipParser()

    def collect(
        self,
        body: str | None,
    ) -> list[Relationship]:

        if not body:
            return []

        return self._parser.parse(
            body,
            source=RelationshipSource.ISSUE_BODY,
        )
