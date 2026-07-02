from __future__ import annotations

from enum import StrEnum


class ScanStatus(StrEnum):
    """
    Lifecycle states of a repository scan.
    """

    QUEUED = "queued"

    RUNNING = "running"

    COMPLETED = "completed"

    FAILED = "failed"

    CANCELLED = "cancelled"
