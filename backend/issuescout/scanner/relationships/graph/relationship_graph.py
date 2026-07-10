from __future__ import annotations

from collections import defaultdict

from issuescout.models.relationships import (
    Relationship,
)


class RelationshipGraph:
    """
    Stores discovered relationships grouped by target number.
    """

    def build(
        self,
        relationships: list[Relationship],
    ) -> dict[int, list[Relationship]]:

        graph: dict[
            int,
            list[Relationship],
        ] = defaultdict(list)

        for relationship in relationships:
            graph[relationship.number].append(
                relationship,
            )

        return dict(graph)
