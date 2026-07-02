from __future__ import annotations

from abc import (
    ABC,
    abstractmethod,
)

from issuescout.models.scan_job import ScanJob


class ScanJobRepository(ABC):
    """
    Abstract repository for scan jobs.
    """

    @abstractmethod
    def add(
        self,
        job: ScanJob,
    ) -> None: ...

    @abstractmethod
    def get(
        self,
        job_id: str,
    ) -> ScanJob | None: ...

    @abstractmethod
    def list(
        self,
    ) -> list[ScanJob]: ...

    @abstractmethod
    def delete(
        self,
        job_id: str,
    ) -> bool: ...

    @abstractmethod
    def clear(
        self,
    ) -> None: ...
