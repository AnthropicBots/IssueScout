from __future__ import annotations

from collections.abc import Iterable

from issuescout.evaluation.comparison.comparator import EvaluationComparator
from issuescout.evaluation.comparison.result import ComparisonResult
from issuescout.evaluation.models import EvaluationRecord


class EvaluationRunner:
    """
    Executes IssueScout evaluation over a collection of evaluation records.
    """

    def __init__(self) -> None:
        self._comparator = EvaluationComparator()

    def run(
        self,
        records: Iterable[EvaluationRecord],
    ) -> list[ComparisonResult]:
        """
        Compare every evaluation record against its ground truth.
        """

        return [self._comparator.compare(record) for record in records]
