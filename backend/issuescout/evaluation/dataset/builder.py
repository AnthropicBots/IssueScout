from __future__ import annotations

from issuescout.evaluation.models import (
    EvaluationRecord,
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
        record: EvaluationRecord,
    ) -> None:
        """
        Add an evaluation record to the dataset.
        """
        self._evaluation.records.append(record)

    def build(
        self,
    ) -> RepositoryEvaluation:
        """
        Return the completed dataset.
        """
        return self._evaluation
