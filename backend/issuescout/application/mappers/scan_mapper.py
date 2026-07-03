from __future__ import annotations

from issuescout.application.dto import ScanDTO
from issuescout.models import ScanResult


class ScanMapper:
    @staticmethod
    def from_result(
        result: ScanResult,
    ) -> ScanDTO:
        return ScanDTO(
            repository=result.repository,
            total_issues=result.total_issues,
            available_issues=result.available_issues,
        )
