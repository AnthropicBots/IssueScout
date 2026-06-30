from __future__ import annotations

from dataclasses import dataclass

from issuescout.evaluation.metrics.summary import EvaluationSummary


@dataclass(slots=True)
class RepositoryBenchmark:
    """
    Benchmark results for one repository.
    """

    repository_owner: str

    repository_name: str

    summary: EvaluationSummary

    @property
    def full_name(self) -> str:
        return f"{self.repository_owner}/{self.repository_name}"
