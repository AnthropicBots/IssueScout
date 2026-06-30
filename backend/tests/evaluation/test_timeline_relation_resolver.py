from __future__ import annotations

from issuescout.evaluation.timeline_relation import (
    TimelineRelation,
)


class TimelineRelationResolver:
    """
    Resolves Issue → Pull Request relationships from GitHub timeline events.

    This class contains no GitHub API calls.
    It only interprets already-fetched timeline events.
    """

    def resolve(
        self,
        timeline: list[dict],
    ) -> TimelineRelation:
        """
        Resolve the best Issue → Pull Request relationship.

        Placeholder implementation.

        The first implementation simply returns an unresolved relation.
        """
        return TimelineRelation(
            pull_request_number=None,
            confidence=0.0,
            evidence=[],
            merged=False,
            closed_issue=False,
            linkage_method="unresolved",
        )
