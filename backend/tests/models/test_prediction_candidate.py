from issuescout.evaluation.models import PredictionCandidate


def test_prediction_candidate_roundtrip():
    candidate = PredictionCandidate(
        pull_request_number=10,
        score=95.5,
        confidence="High",
        rank=1,
    )

    restored = PredictionCandidate.from_dict(
        candidate.to_dict(),
    )

    assert restored == candidate
