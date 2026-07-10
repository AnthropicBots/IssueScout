from __future__ import annotations

from dataclasses import dataclass, field

from issuescout.models.relationships.relationship_source import (
    RelationshipSource,
)
from issuescout.models.relationships.relationship_target import (
    RelationshipTarget,
)
from issuescout.models.relationships.relationship_type import (
    RelationshipType,
)


@dataclass(slots=True)
class Relationship:
    """
    Represents a discovered relationship between GitHub entities.
    """

    number: int

    target: RelationshipTarget

    relationship_type: RelationshipType

    source: RelationshipSource

    confidence: float = 0.0

    repository: str | None = None

    owner: str | None = None

    url: str | None = None

    evidence: list[str] = field(default_factory=list)

    raw_text: str | None = None

    event_type: str | None = None

    actor: str | None = None

    created_at: str | None = None
