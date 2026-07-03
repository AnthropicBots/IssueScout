from issuescout.models.explanation import (
    ExplanationItem,
    PredictionExplanation,
)


def test_explanation_item():
    item = ExplanationItem(
        analyzer="title",
        score=10,
        confidence=90,
        reason="Matched",
    )

    assert item.evidence_type == "supporting"


def test_prediction_explanation():
    explanation = PredictionExplanation(
        summary="Good match",
        confidence="High",
        total_score=95,
    )

    assert explanation.items == []
    assert explanation.summary == "Good match"
