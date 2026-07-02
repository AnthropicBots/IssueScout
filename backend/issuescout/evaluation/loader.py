from __future__ import annotations

import json
from pathlib import Path

from issuescout.evaluation.models import (
    EvaluationRecord,
    GroundTruthRecord,
    PredictionCandidate,
    RepositoryEvaluation,
)


class EvaluationLoader:
    """
    Loads evaluation datasets.

    Currently supports the legacy JSON dataset format.

    The loader converts external dataset files into the internal
    GroundTruthRecord model so that future storage formats
    (CSV, SQLite, API, etc.) can reuse the same evaluation pipeline.
    """

    def load(
        self,
        path: str | Path,
    ) -> RepositoryEvaluation:
        """
        Load an evaluation dataset.

        Parameters
        ----------
        path:
            Path to a dataset file.

        Returns
        -------
        RepositoryEvaluation
        """

        path = Path(path)

        with path.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        # ------------------------------------------------------------------
        # Native RepositoryEvaluation format
        # ------------------------------------------------------------------
        if "repository_owner" in data and "repository_name" in data:
            return RepositoryEvaluation.from_dict(data)

        # ------------------------------------------------------------------
        # Legacy JSON format
        # ------------------------------------------------------------------
        repository = data["repository"]

        if "/" in repository:
            owner, repo = repository.split("/", 1)
        else:
            owner = ""
            repo = repository

        records: list[EvaluationRecord] = []

        for record in data.get(
            "records",
            [],
        ):
            predictions = [
                PredictionCandidate(
                    pull_request_number=prediction["pull_request_number"],
                    score=prediction["score"],
                    confidence=prediction["confidence"],
                    rank=prediction["rank"],
                    matched=prediction.get(
                        "matched",
                        False,
                    ),
                )
                for prediction in record.get(
                    "predictions",
                    [],
                )
            ]

            ground_truth = GroundTruthRecord(
                repository_owner=owner,
                repository_name=repo,
                issue_number=record["issue_number"],
                issue_title=record.get(
                    "issue_title",
                    "",
                ),
                issue_state=record.get(
                    "issue_state",
                    "closed",
                ),
                actual_pull_request=record.get(
                    "actual_pull_request",
                ),
                linkage_method=record.get(
                    "linkage_method",
                    "legacy_json",
                ),
            )

            records.append(
                EvaluationRecord(
                    ground_truth=ground_truth,
                    predictions=predictions,
                )
            )

        return RepositoryEvaluation(
            repository_owner=owner,
            repository_name=repo,
            records=records,
        )
