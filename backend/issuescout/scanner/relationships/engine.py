from __future__ import annotations

from issuescout.models.relationships import (
    Relationship,
)
from issuescout.scanner.relationships.collectors import (
    BodyRelationshipCollector,
    CommentRelationshipCollector,
    TimelineRelationshipCollector,
)
from issuescout.scanner.relationships.evaluation.relationship_evaluator import (
    RelationshipEvaluator,
)
from issuescout.scanner.relationships.graph.relationship_graph import (
    RelationshipGraph,
)


class RelationshipEngine:
    """
    Discovers semantic GitHub relationships from every
    available issue source.
    """

    def __init__(self) -> None:
        self.body = BodyRelationshipCollector()
        self.comments = CommentRelationshipCollector()
        self.timeline = TimelineRelationshipCollector()

        self.evaluator = RelationshipEvaluator()
        self.graph = RelationshipGraph()

    def collect(
        self,
        *,
        body: str | None,
        comments: list[dict],
        timeline: list[dict],
    ) -> list[Relationship]:

        relationships: list[Relationship] = []

        relationships.extend(self.body.collect(body))

        relationships.extend(self.comments.collect(comments))

        relationships.extend(self.timeline.collect(timeline))

        evaluated = [
            self.evaluator.evaluate(
                relationship,
            )
            for relationship in relationships
        ]

        return sorted(
            evaluated,
            key=lambda relationship: relationship.confidence,
            reverse=True,
        )
