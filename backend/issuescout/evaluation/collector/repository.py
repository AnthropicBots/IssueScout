from __future__ import annotations

from issuescout.evaluation.dataset.builder import DatasetBuilder
from issuescout.evaluation.models import GroundTruthRecord


class RepositoryCollector:
    """
    Collects all ground-truth records belonging to a repository.
    """

    def __init__(
        self,
        repository_owner: str,
        repository_name: str,
    ) -> None:

        self.repository_owner = repository_owner
        self.repository_name = repository_name

    def build_dataset(
        self,
        records: list[GroundTruthRecord],
    ):
        builder = DatasetBuilder(
            repository_owner=self.repository_owner,
            repository_name=self.repository_name,
        )

        for record in records:
            builder.add_record(
                record,
            )

        return builder.build()
