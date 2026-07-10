from __future__ import annotations

from issuescout.models.relationships import (
    Relationship,
    RelationshipSource,
)
from issuescout.scanner.relationships.parsers import (
    GitHubRelationshipParser,
)


class CommitRelationshipCollector:
    """
    Collects relationships from commit messages.
    """

    def __init__(self) -> None:
        self._parser = GitHubRelationshipParser()

    def collect(
        self,
        commits: list[dict],
    ) -> list[Relationship]:

        relationships: list[Relationship] = []

        for commit in commits:
            message = commit.get("commit", {}).get("message", "")

            relationships.extend(
                self._parser.parse(
                    message,
                    source=RelationshipSource.COMMIT_MESSAGE,
                )
            )

        return relationships
