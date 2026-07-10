from __future__ import annotations

from issuescout.models.relationships import (
    Relationship,
    RelationshipSource,
)
from issuescout.scanner.relationships.parsers import (
    GitHubRelationshipParser,
)


class TimelineRelationshipCollector:
    """
    Collects relationships from timeline events.

    Both structured events and free-text payloads
    are analysed.
    """

    def __init__(self) -> None:
        self._parser = GitHubRelationshipParser()

    def collect(
        self,
        timeline: list[dict],
    ) -> list[Relationship]:

        relationships: list[Relationship] = []

        for event in timeline:
            relationships.extend(
                self._parser.parse_timeline_event(
                    event,
                )
            )

            relationships.extend(
                self._parser.parse(
                    str(event),
                    source=RelationshipSource.ISSUE_TIMELINE,
                )
            )

        return relationships
