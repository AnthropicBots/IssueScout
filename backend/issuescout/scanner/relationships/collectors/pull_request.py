from __future__ import annotations

from issuescout.models.relationships import (
    Relationship,
    RelationshipSource,
)
from issuescout.scanner.relationships.parsers import (
    GitHubRelationshipParser,
)


class PullRequestRelationshipCollector:
    """
    Collects relationships from pull request descriptions.
    """

    def __init__(self) -> None:
        self._parser = GitHubRelationshipParser()

    def collect(
        self,
        body: str | None,
    ) -> list[Relationship]:

        return self._parser.parse(
            body or "",
            source=RelationshipSource.PULL_REQUEST_BODY,
        )
