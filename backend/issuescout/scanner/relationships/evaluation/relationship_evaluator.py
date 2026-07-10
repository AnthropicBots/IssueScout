from __future__ import annotations

from issuescout.models.relationships import (
    Relationship,
    RelationshipType,
)


class RelationshipEvaluator:
    """
    Assigns a confidence score to discovered relationships.
    """

    _CONFIDENCE = {
        RelationshipType.FIXES: 1.00,
        RelationshipType.CLOSES: 0.98,
        RelationshipType.RESOLVES: 0.97,
        RelationshipType.DUPLICATE: 0.92,
        RelationshipType.DEPENDS_ON: 0.88,
        RelationshipType.BLOCKED_BY: 0.88,
        RelationshipType.SUPERSEDED_BY: 0.85,
        RelationshipType.LINKED: 0.82,
        RelationshipType.CROSS_REFERENCED: 0.76,
        RelationshipType.RELATED: 0.62,
        RelationshipType.REFERENCES: 0.48,
        RelationshipType.MENTIONS: 0.30,
        RelationshipType.UNKNOWN: 0.10,
    }

    def evaluate(
        self,
        relationship: Relationship,
    ) -> Relationship:

        relationship.confidence = self._CONFIDENCE.get(
            relationship.relationship_type,
            0.10,
        )

        return relationship
