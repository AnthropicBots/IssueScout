from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from pathlib import Path

from issuescout.evaluation.metrics.summary import EvaluationSummary


class EvaluationGateway(ABC):
    @abstractmethod
    def evaluate_dataset(
        self,
        dataset: str | Path,
    ) -> EvaluationSummary:
        """
        Evaluate a dataset.
        """
