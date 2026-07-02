from issuescout.models.scan_job import ScanJob
from issuescout.repositories.scan_job_repository import (
    ScanJobRepository,
)


class InMemoryScanJobRepository(
    ScanJobRepository,
):
    """
    In-memory implementation of the scan job repository.
    """

    def __init__(
        self,
    ) -> None:
        self._jobs: dict[
            str,
            ScanJob,
        ] = {}

    def add(
        self,
        job: ScanJob,
    ) -> None:
        self._jobs[job.job_id] = job

    def get(
        self,
        job_id: str,
    ) -> ScanJob | None:
        return self._jobs.get(
            job_id,
        )

    def list(
        self,
    ) -> list[ScanJob]:
        return list(reversed(list(self._jobs.values())))

    def delete(
        self,
        job_id: str,
    ) -> bool:
        return (
            self._jobs.pop(
                job_id,
                None,
            )
            is not None
        )

    def clear(
        self,
    ) -> None:
        self._jobs.clear()
