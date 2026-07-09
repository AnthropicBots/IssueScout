from __future__ import annotations

from datetime import datetime, timezone
from typing import cast
from issuescout.models import (
    AnalysisResult,
    Issue,
)


class ConfidenceCalculator:
    """
    Calculates a contributor confidence score (0-100).

    Unlike the filtering pipeline, this score estimates
    how attractive an issue is for contributors.
    """

    def calculate(
        self,
        issue_or_results: Issue | list[AnalysisResult],
        results: list[AnalysisResult] | None = None,
    ) -> int:
        """
        Calculate contributor confidence.

        Supports both signatures:

            calculate(results)
            calculate(issue, results)
        """

        # --------------------------------------------------
        # Legacy behaviour
        # --------------------------------------------------

        if results is None:
            legacy_results = cast(
                list[AnalysisResult],
                issue_or_results,
            )

            return sum(result.score for result in legacy_results if result.passed)

        issue = cast(
            Issue,
            issue_or_results,
        )

        score = 0

        # --------------------------------------------------
        # Analyzer results
        # --------------------------------------------------

        assignment = next(
            (r for r in results if r.analyzer == "assignment"),
            None,
        )

        linked_pr = next(
            (r for r in results if r.analyzer == "linked_pr"),
            None,
        )

        if assignment and assignment.passed:
            score += 20

        if linked_pr and linked_pr.passed:
            score += 20

        # --------------------------------------------------
        # Labels
        # --------------------------------------------------

        labels = {label.lower() for label in issue.labels}

        if "good first issue" in labels:
            score += 20

        if "help wanted" in labels:
            score += 10

        if len(labels) >= 3:
            score += 5

        # --------------------------------------------------
        # Milestone
        # --------------------------------------------------

        if issue.milestone:
            score += 5

        # --------------------------------------------------
        # Recent activity
        # --------------------------------------------------

        if issue.updated_at is not None:
            days = (datetime.now(timezone.utc) - issue.updated_at).days

            if days <= 30:
                score += 15
            elif days <= 90:
                score += 8

        return score
