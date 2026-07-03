from __future__ import annotations

from issuescout.repositories.in_memory_scan_job_repository import (
    InMemoryScanJobRepository,
)
from issuescout.repositories.scan_job_repository import (
    ScanJobRepository,
)


def create_scan_job_repository() -> ScanJobRepository:
    """
    Create the application's scan job repository.

    This factory centralizes repository creation so the
    implementation can later be switched to SQLite or
    PostgreSQL without changing service code.
    """

    return InMemoryScanJobRepository()
