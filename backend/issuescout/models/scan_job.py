from __future__ import annotations

from dataclasses import dataclass, field
from datetime import (
    UTC,
    datetime,
)
from uuid import uuid4

from issuescout.models import ScanResult
from issuescout.models.scan_status import ScanStatus


@dataclass(slots=True)
class ScanJob:
    """
    Represents a repository scan job.
    """

    owner: str

    repository: str

    job_id: str = field(default_factory=lambda: str(uuid4()))

    status: ScanStatus = ScanStatus.QUEUED

    processed_issues: int = 0

    total_issues: int = 0

    progress: int = 0

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            UTC,
        ),
    )

    started_at: datetime | None = None

    completed_at: datetime | None = None

    result: ScanResult | None = None

    error: str | None = None
