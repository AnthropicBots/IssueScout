from __future__ import annotations

from issuescout.evaluation.models import (
    EvaluationRecord,
    GroundTruthRecord,
    RepositoryEvaluation,
)


class DatasetBuilder:
    """
    Builds evaluation datasets incrementally.

    A dataset represents all evaluation records belonging to a single
    repository.
    """

    def __init__(
        self,
        repository_owner: str,
        repository_name: str,
    ) -> None:
        self._evaluation = RepositoryEvaluation(
            repository_owner=repository_owner,
            repository_name=repository_name,
        )

    def add_record(
        self,
        record: EvaluationRecord | GroundTruthRecord,
    ) -> None:
        """
        Add a record to the evaluation dataset.

        Ground-truth records are automatically wrapped into an
        EvaluationRecord with an empty prediction list.
        """

        if isinstance(
            record,
            GroundTruthRecord,
        ):
            record = EvaluationRecord(
                ground_truth=record,
                predictions=[],
            )

        self._evaluation.records.append(
            record,
        )

    def build(
        self,
    ) -> RepositoryEvaluation:
        """
        Return the completed dataset.
        """
        return self._evaluation
