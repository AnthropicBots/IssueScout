from __future__ import annotations

from issuescout.evaluation.models import RepositoryEvaluation


class DatasetValidator:
    """
    Performs basic validation of evaluation datasets.
    """

    def validate(
        self,
        dataset: RepositoryEvaluation,
    ) -> list[str]:
        errors: list[str] = []

        if not dataset.repository_owner:
            errors.append("Repository owner is missing.")

        if not dataset.repository_name:
            errors.append("Repository name is missing.")

        if not dataset.records:
            errors.append("Dataset contains no evaluation records.")

        return errors

    def is_valid(
        self,
        dataset: RepositoryEvaluation,
    ) -> bool:
        return not self.validate(dataset)
