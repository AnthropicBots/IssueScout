from __future__ import annotations

from enum import StrEnum


class RelationshipType(StrEnum):
    """
    Semantic relationship between two GitHub entities.
    """

    # Closing relationships
    CLOSES = "closes"
    FIXES = "fixes"
    RESOLVES = "resolves"

    # General references
    REFERENCES = "references"
    MENTIONS = "mentions"
    RELATED = "related"

    # Workflow relationships
    DUPLICATE = "duplicate"
    DEPENDS_ON = "depends_on"
    BLOCKED_BY = "blocked_by"
    SUPERSEDED_BY = "superseded_by"

    # Timeline relationships
    LINKED = "linked"
    CROSS_REFERENCED = "cross_referenced"

    # Fallback
    UNKNOWN = "unknown"
