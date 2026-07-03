from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from issuescout.models import ScanResult


class ScannerGateway(ABC):
    @abstractmethod
    async def scan_repository(
        self,
        owner: str,
        repository: str,
    ) -> ScanResult:
        """
        Scan a repository.
        """
