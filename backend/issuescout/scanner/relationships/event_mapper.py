from __future__ import annotations

from issuescout.models.relationships import RelationshipType


_EVENT_MAP: dict[str, RelationshipType] = {
    "cross-referenced": RelationshipType.CROSS_REFERENCED,
    "connected": RelationshipType.LINKED,
    "referenced": RelationshipType.REFERENCES,
    "mentioned": RelationshipType.MENTIONS,
    "closed": RelationshipType.CLOSES,
    "merged": RelationshipType.CLOSES,
}


def relationship_type_for_event(
    event: str | None,
) -> RelationshipType:
    """
    Maps GitHub timeline events to semantic
    relationship types.
    """

    if event is None:
        return RelationshipType.UNKNOWN

    return _EVENT_MAP.get(
        event,
        RelationshipType.UNKNOWN,
    )
