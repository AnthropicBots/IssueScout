from __future__ import annotations

from issuescout.evaluation.timeline_relation import (
    TimelineEvidence,
    TimelineRelation,
)
from issuescout.evaluation.scoring.timeline import TimelineEvidenceScorer


class TimelineRelationResolver:
    """
    Resolves Issue → Pull Request relationships from GitHub timeline events.

    The resolver is completely independent of the GitHub API.
    It operates only on timeline event dictionaries that have already been
    fetched by the TimelineService.
    """

    def __init__(self) -> None:
        self._scorer = TimelineEvidenceScorer()

    def _select_best_candidate(
        self,
        evidence: list[TimelineEvidence],
    ) -> TimelineEvidence:
        """
        Select the strongest candidate from all collected evidence.
        """

        return max(
            evidence,
            key=self._scorer.score,
        )

    def resolve(
        self,
        timeline: list[dict],
    ) -> TimelineRelation:
        evidence: list[TimelineEvidence] = []
        closed_issue = False

        for event in timeline:
            event_type = event.get("event")

            if event_type == "closed":
                closed_issue = True
                continue

            if event_type == "referenced":
                continue

            if event_type != "cross-referenced":
                continue

            source = event.get("source") or {}
            issue = source.get("issue") or {}

            if "pull_request" not in issue:
                continue

            pull_request_number = issue.get("number")

            if pull_request_number is None:
                continue

            evidence.append(
                TimelineEvidence(
                    event_type="cross-referenced",
                    source="timeline",
                    pull_request_number=pull_request_number,
                    confidence=1.0,
                )
            )

        if not evidence:
            return TimelineRelation(
                pull_request_number=None,
                confidence=0.0,
                evidence=[],
                closed_issue=closed_issue,
                linkage_method="unresolved",
            )

        best = self._select_best_candidate(evidence)

        return TimelineRelation(
            pull_request_number=best.pull_request_number,
            confidence=best.confidence,
            evidence=evidence,
            closed_issue=closed_issue,
            linkage_method="cross-referenced",
        )
