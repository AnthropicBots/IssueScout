from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class PredictionDTO:
    issue_number: int
    pull_request_number: int | None
    confidence: float
    accepted: bool
