from __future__ import annotations

from issuescout.evaluation.scoring.weights import TimelineScoringWeights
from issuescout.evaluation.timeline_relation import TimelineEvidence


class TimelineEvidenceScorer:
    """
    Scores timeline evidence.

    The scorer converts one piece of evidence into a numerical score.
    """

    def __init__(
        self,
        weights: TimelineScoringWeights | None = None,
    ) -> None:
        self._weights = weights or TimelineScoringWeights()

    def score(
        self,
        evidence: TimelineEvidence,
    ) -> float:

        if evidence.event_type == "cross-referenced":
            return self._weights.cross_referenced

        if evidence.event_type == "referenced":
            return self._weights.referenced

        return evidence.confidence
