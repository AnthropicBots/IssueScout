from __future__ import annotations

from issuescout.evaluation.models import GroundTruthRecord


class GroundTruthCollector:
    """
    Base interface for all ground-truth collectors.
    """

    def collect(
        self,
        *args,
        **kwargs,
    ) -> GroundTruthRecord:
        raise NotImplementedError
