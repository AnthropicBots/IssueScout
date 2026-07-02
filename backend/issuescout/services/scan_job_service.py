from __future__ import annotations

from datetime import (
    UTC,
    datetime,
)

from issuescout.models.scan_job import ScanJob
from collections import Counter

from issuescout.models.scan_status import ScanStatus
from issuescout.scanner.engine import ScannerEngine
from issuescout.repositories import (
    InMemoryScanJobRepository,
    ScanJobRepository,
)


class ScanJobService:
    """
    Service responsible for managing repository scan jobs.
    """

    def __init__(
        self,
        repository: ScanJobRepository | None = None,
    ) -> None:
        self._repository = repository or InMemoryScanJobRepository()

    def create_job(
        self,
        owner: str,
        repository: str,
    ) -> ScanJob:

        job = ScanJob(
            owner=owner,
            repository=repository,
        )

        self._repository.add(
            job,
        )

        return job

    def get_job(
        self,
        job_id: str,
    ) -> ScanJob | None:

        return self._repository.get(
            job_id,
        )

    async def run_job(
        self,
        job: ScanJob,
    ) -> None:

        job.status = ScanStatus.RUNNING

        job.started_at = datetime.now(
            UTC,
        )

        try:
            engine = ScannerEngine()

            def update_progress(
                processed: int,
                total: int,
            ) -> None:
                job.processed_issues = processed

                job.total_issues = total

                if total > 0:
                    job.progress = int((processed / total) * 100)
                else:
                    job.progress = 0

            job.result = await engine.scan_repository(
                job.owner,
                job.repository,
                progress_callback=update_progress,
            )

            job.progress = 100

            job.processed_issues = job.total_issues

            job.status = ScanStatus.COMPLETED

        except Exception as exc:
            job.status = ScanStatus.FAILED

            job.error = str(exc)

        finally:
            job.completed_at = datetime.now(
                UTC,
            )

    def get_job_status(
        self,
        job_id: str,
    ) -> ScanJob | None:
        """
        Return a scan job by its identifier.
        """
        return self._repository.get(
            job_id,
        )

    def get_job_result(
        self,
        job_id: str,
    ) -> ScanJob | None:
        """
        Return the scan job for retrieving its result.
        """
        return self._repository.get(
            job_id,
        )

    def list_jobs(
        self,
    ) -> list[ScanJob]:
        """
        Return all scan jobs ordered from newest to oldest.
        """
        return self._repository.list()

    def find_jobs(
        self,
        *,
        status: ScanStatus | None = None,
        owner: str | None = None,
        repository: str | None = None,
        limit: int | None = None,
        offset: int = 0,
    ) -> list[ScanJob]:

        jobs = self.list_jobs()

        if status is not None:
            jobs = [job for job in jobs if job.status == status]

        if owner is not None:
            jobs = [job for job in jobs if job.owner == owner]

        if repository is not None:
            jobs = [job for job in jobs if job.repository == repository]

        jobs = jobs[offset:]

        if limit is not None:
            jobs = jobs[:limit]

        return jobs

    def get_statistics(
        self,
    ) -> dict[str, int]:
        """
        Return summary statistics for scan jobs.
        """

        counts = Counter(job.status for job in self._repository.list())

        return {
            "total_jobs": len(
                self._repository.list(),
            ),
            "queued_jobs": counts[ScanStatus.QUEUED],
            "running_jobs": counts[ScanStatus.RUNNING],
            "completed_jobs": counts[ScanStatus.COMPLETED],
            "failed_jobs": counts[ScanStatus.FAILED],
        }

    def delete_job(
        self,
        job_id: str,
    ) -> bool:
        """
        Delete a scan job.

        Returns True if the job existed and was deleted,
        otherwise returns False.
        """
        return self._repository.delete(
            job_id,
        )

    def cancel_job(
        self,
        job_id: str,
    ) -> ScanJob | None:
        """
        Cancel a queued or running scan job.
        """
        job = self._repository.get(
            job_id,
        )

        if job is None:
            return None

        if job.status not in (
            ScanStatus.QUEUED,
            ScanStatus.RUNNING,
        ):
            return job

        job.status = ScanStatus.CANCELLED

        job.completed_at = datetime.now(
            UTC,
        )

        job.progress = 0

        return job

    def clear(self) -> None:
        """
        Remove all stored scan jobs.

        Primarily intended for use by the test suite to ensure
        isolation between test cases.
        """
        self._repository.clear()
