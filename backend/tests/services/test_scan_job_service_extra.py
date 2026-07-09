from unittest.mock import AsyncMock
from unittest.mock import Mock

import pytest

from issuescout.models.scan_status import ScanStatus
from issuescout.services.scan_job_service import (
    ScanJobService,
)

pytestmark = pytest.mark.anyio


async def test_run_job_success():

    engine = Mock()

    engine.scan_repository = AsyncMock(
        return_value={
            "repository": "python/cpython",
        },
    )

    service = ScanJobService(
        scanner_engine=engine,
    )

    job = service.create_job(
        "python",
        "cpython",
    )

    await service.run_job(job)

    assert job.status == ScanStatus.COMPLETED
    assert job.progress == 100
    assert job.result == {
        "repository": "python/cpython",
    }
    assert job.started_at is not None
    assert job.completed_at is not None


async def test_run_job_failure():

    engine = Mock()

    engine.scan_repository = AsyncMock(
        side_effect=RuntimeError(
            "boom",
        ),
    )

    service = ScanJobService(
        scanner_engine=engine,
    )

    job = service.create_job(
        "python",
        "cpython",
    )

    await service.run_job(job)

    assert job.status == ScanStatus.FAILED
    assert job.error == "boom"
    assert job.completed_at is not None


async def test_progress_callback_updates_job():

    async def fake_scan(
        owner,
        repository,
        *,
        progress_callback,
    ):
        progress_callback(
            3,
            10,
        )

        return {}

    engine = Mock()

    engine.scan_repository = AsyncMock(
        side_effect=fake_scan,
    )

    service = ScanJobService(
        scanner_engine=engine,
    )

    job = service.create_job(
        "python",
        "cpython",
    )

    await service.run_job(job)

    assert job.total_issues == 10
    assert job.processed_issues == 10
    assert job.progress == 100


def test_get_statistics():

    service = ScanJobService()

    queued = service.create_job(
        "python",
        "cpython",
    )

    running = service.create_job(
        "fastapi",
        "fastapi",
    )

    completed = service.create_job(
        "django",
        "django",
    )

    failed = service.create_job(
        "pallets",
        "flask",
    )

    queued.status = ScanStatus.QUEUED
    running.status = ScanStatus.RUNNING
    completed.status = ScanStatus.COMPLETED
    failed.status = ScanStatus.FAILED

    stats = service.get_statistics()

    assert stats["total_jobs"] == 4
    assert stats["queued_jobs"] == 1
    assert stats["running_jobs"] == 1
    assert stats["completed_jobs"] == 1
    assert stats["failed_jobs"] == 1


def test_find_jobs_limit():

    service = ScanJobService()

    service.create_job(
        "one",
        "repo",
    )

    second = service.create_job(
        "two",
        "repo",
    )

    jobs = service.find_jobs(
        limit=1,
    )

    assert jobs == [second]


def test_find_jobs_offset():

    service = ScanJobService()

    third = service.create_job(
        "one",
        "repo",
    )

    second = service.create_job(
        "two",
        "repo",
    )

    service.create_job(
        "three",
        "repo",
    )

    jobs = service.find_jobs(
        offset=1,
    )

    assert jobs == [
        second,
        third,
    ]
