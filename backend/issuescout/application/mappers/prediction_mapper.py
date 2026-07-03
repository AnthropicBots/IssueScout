from __future__ import annotations

from issuescout.application.dto import PredictionDTO
from issuescout.models.analysis import PredictionResult


class PredictionMapper:
    @staticmethod
    def from_result(
        prediction: PredictionResult,
    ) -> PredictionDTO:
        return PredictionDTO(
            issue_number=prediction.issue_number,
            pull_request_number=(
                prediction.prediction.pull_request.number
                if prediction.prediction
                else None
            ),
            # PredictionResult stores confidence as a string.
            # DTO expects a numeric value.
            confidence=0.0,
            accepted=prediction.accepted,
        )
