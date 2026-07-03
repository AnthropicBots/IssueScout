from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class EvaluationDTO:
    accuracy: float
    precision: float
    recall: float
    mrr: float
    map_score: float
