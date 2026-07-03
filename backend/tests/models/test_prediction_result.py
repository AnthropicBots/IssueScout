from issuescout.models.analysis import PredictionResult


def test_prediction_result_defaults():
    result = PredictionResult(
        issue_number=10,
    )

    assert result.prediction is None
    assert result.accepted is False
    assert result.candidates == []
    assert result.evidence == []
    assert result.confidence == "Very Low"
