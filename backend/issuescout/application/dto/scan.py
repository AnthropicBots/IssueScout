from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ScanDTO:
    repository: str
    total_issues: int
    available_issues: int
