from issuescout.evaluation.scoring.timeline import TimelineEvidenceScorer
from issuescout.evaluation.timeline_relation import TimelineEvidence


def test_cross_reference_weight():
    scorer = TimelineEvidenceScorer()

    evidence = TimelineEvidence(
        event_type="cross-referenced",
        source="timeline",
        pull_request_number=1,
        confidence=0.1,
    )

    assert scorer.score(evidence) == 1.0


def test_referenced_weight():
    scorer = TimelineEvidenceScorer()

    evidence = TimelineEvidence(
        event_type="referenced",
        source="timeline",
        pull_request_number=1,
        confidence=1.0,
    )

    assert scorer.score(evidence) == 0.4


def test_unknown_event_uses_confidence():
    scorer = TimelineEvidenceScorer()

    evidence = TimelineEvidence(
        event_type="unknown",
        source="timeline",
        pull_request_number=1,
        confidence=0.73,
    )

    assert scorer.score(evidence) == 0.73
