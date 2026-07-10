from __future__ import annotations

import re

from issuescout.models.relationships import (
    Relationship,
    RelationshipSource,
    RelationshipTarget,
    RelationshipType,
)
from issuescout.scanner.relationships.event_mapper import (
    relationship_type_for_event,
)


class GitHubRelationshipParser:
    """
    Parses GitHub issue and pull request references
    from free-form text.
    """

    _PATTERNS: list[
        tuple[
            RelationshipType,
            re.Pattern[str],
        ]
    ] = [
        (
            RelationshipType.FIXES,
            re.compile(
                r"\bfix(?:e[sd]?|ing)?\s+#(\d+)",
                re.IGNORECASE,
            ),
        ),
        (
            RelationshipType.CLOSES,
            re.compile(
                r"\bclose[sd]?\s+#(\d+)",
                re.IGNORECASE,
            ),
        ),
        (
            RelationshipType.RESOLVES,
            re.compile(
                r"\bresolve[sd]?\s+#(\d+)",
                re.IGNORECASE,
            ),
        ),
        (
            RelationshipType.RELATED,
            re.compile(
                r"\brelated\s+to\s+#(\d+)",
                re.IGNORECASE,
            ),
        ),
        (
            RelationshipType.DUPLICATE,
            re.compile(
                r"\bduplicate\s+of\s+#(\d+)",
                re.IGNORECASE,
            ),
        ),
        (
            RelationshipType.DEPENDS_ON,
            re.compile(
                r"\bdepends\s+on\s+#(\d+)",
                re.IGNORECASE,
            ),
        ),
        (
            RelationshipType.BLOCKED_BY,
            re.compile(
                r"\bblocked\s+by\s+#(\d+)",
                re.IGNORECASE,
            ),
        ),
        (
            RelationshipType.SUPERSEDED_BY,
            re.compile(
                r"\bsuperseded\s+by\s+#(\d+)",
                re.IGNORECASE,
            ),
        ),
    ]

    _GENERIC_REFERENCE = re.compile(
        r"(?:PR\s*#|Issue\s*#|GH-|\#)(\d+)",
        re.IGNORECASE,
    )

    def parse(
        self,
        text: str,
        *,
        source: RelationshipSource,
    ) -> list[Relationship]:

        relationships: list[Relationship] = []

        discovered: set[
            tuple[
                int,
                RelationshipType,
            ]
        ] = set()

        for relationship_type, pattern in self._PATTERNS:
            for match in pattern.finditer(text):
                number = int(match.group(1))

                key = (
                    number,
                    relationship_type,
                )

                if key in discovered:
                    continue

                discovered.add(key)

                relationships.append(
                    Relationship(
                        number=number,
                        target=RelationshipTarget.UNKNOWN,
                        relationship_type=relationship_type,
                        source=source,
                        raw_text=match.group(0),
                    )
                )

        for match in self._GENERIC_REFERENCE.finditer(
            text,
        ):
            number = int(match.group(1))

            key = (
                number,
                RelationshipType.REFERENCES,
            )

            if key in discovered:
                continue

            discovered.add(key)

            relationships.append(
                Relationship(
                    number=number,
                    target=RelationshipTarget.UNKNOWN,
                    relationship_type=RelationshipType.REFERENCES,
                    source=source,
                    raw_text=match.group(0),
                )
            )

        return relationships

    def parse_timeline_event(
        self,
        event: dict,
    ) -> list[Relationship]:
        """
        Parse structured GitHub timeline events.
        """

        relationships: list[Relationship] = []

        event_type = event.get("event")

        source = event.get("source")

        if not isinstance(source, dict):
            return relationships

        issue = source.get("issue")

        if not isinstance(issue, dict):
            return relationships

        number = issue.get("number")

        if not isinstance(number, int):
            return relationships

        relationships.append(
            Relationship(
                number=number,
                target=RelationshipTarget.UNKNOWN,
                relationship_type=relationship_type_for_event(
                    event_type,
                ),
                source=RelationshipSource.ISSUE_TIMELINE,
                event_type=event_type,
                actor=(event.get("actor", {}).get("login")),
                created_at=event.get("created_at"),
            )
        )

        return relationships
