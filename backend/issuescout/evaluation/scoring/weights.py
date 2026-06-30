from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TimelineScoringWeights:
    """
    Default weights used when scoring timeline evidence.

    These values are intentionally centralized so they can later be
    tuned using benchmark results without changing resolver logic.
    """

    cross_referenced: float = 1.00

    referenced: float = 0.40

    merged_bonus: float = 0.30

    closed_bonus: float = 0.20

    linked_pr_bonus: float = 0.50
