from __future__ import annotations

from abc import ABC, abstractmethod

from issuescout.models import (
    Issue,
    PullRequest,
)
from issuescout.models.analysis import PredictionResult


class PredictionGateway(ABC):
    @abstractmethod
    async def predict(
        self,
        issue: Issue,
        pull_requests: list[PullRequest],
        *,
        verbose: bool = False,
    ) -> PredictionResult:
        """
        Predict the linked pull request.
        """
