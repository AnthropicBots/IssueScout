from __future__ import annotations

from issuescout.application.dto import EvaluationDTO
from issuescout.evaluation.metrics.summary import EvaluationSummary


class EvaluationMapper:
    @staticmethod
    def from_summary(
        summary: EvaluationSummary,
    ) -> EvaluationDTO:
        return EvaluationDTO(
            accuracy=summary.accuracy,
            precision=summary.precision,
            recall=summary.recall,
            mrr=summary.mrr,
            map_score=summary.map,
        )
