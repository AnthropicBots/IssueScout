from __future__ import annotations

from .model import (
    EvidenceItem,
    EvidenceSummary,
)


def passed(
    summary: EvidenceSummary,
) -> list[EvidenceItem]:
    return summary.passed_items


def failed(
    summary: EvidenceSummary,
) -> list[EvidenceItem]:
    return summary.failed_items


def total_weight(
    summary: EvidenceSummary,
) -> int:
    return summary.total_weight


def passed_weight(
    summary: EvidenceSummary,
) -> int:
    return summary.passed_weight


def failed_weight(
    summary: EvidenceSummary,
) -> int:
    return summary.failed_weight
