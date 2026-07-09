from __future__ import annotations

from dataclasses import dataclass, field

from issuescout.evidence import (
    EvidenceSummary,
)


@dataclass(slots=True)
class ResolutionAnalysisResult:
    """
    Result of analysing whether a pull request
    resolves an issue.
    """

    confidence: int

    reasons: list[str] = field(
        default_factory=list,
    )

    passed_checks: list[str] = field(
        default_factory=list,
    )

    evidence: EvidenceSummary = field(
        default_factory=EvidenceSummary,
    )

    verdict: str = "Unknown"
