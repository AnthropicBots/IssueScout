from issuescout.services.scan_job_service import ScanJobService
from issuescout.models.scan_status import ScanStatus


def test_list_jobs_empty():
    service = ScanJobService()

    assert service.list_jobs() == []


def test_list_jobs_returns_all_jobs():
    service = ScanJobService()

    first = service.create_job(
        "python",
        "cpython",
    )

    second = service.create_job(
        "fastapi",
        "fastapi",
    )

    jobs = service.list_jobs()

    assert len(jobs) == 2

    assert first in jobs

    assert second in jobs


def test_list_jobs_sorted_newest_first():
    service = ScanJobService()

    first = service.create_job(
        "python",
        "cpython",
    )

    second = service.create_job(
        "fastapi",
        "fastapi",
    )

    jobs = service.list_jobs()

    assert jobs[0] == second

    assert jobs[1] == first


def test_get_job_status_returns_job():
    service = ScanJobService()

    job = service.create_job(
        "python",
        "cpython",
    )

    assert service.get_job_status(job.job_id) is job


def test_get_job_result_returns_job():
    service = ScanJobService()

    job = service.create_job(
        "python",
        "cpython",
    )

    assert service.get_job_result(job.job_id) is job


def test_clear_removes_all_jobs():
    service = ScanJobService()

    service.create_job(
        "python",
        "cpython",
    )

    service.create_job(
        "fastapi",
        "fastapi",
    )

    assert len(service.list_jobs()) == 2

    service.clear()

    assert service.list_jobs() == []


def test_delete_existing_job():
    service = ScanJobService()

    job = service.create_job(
        "python",
        "cpython",
    )

    deleted = service.delete_job(
        job.job_id,
    )

    assert deleted is True

    assert (
        service.get_job(
            job.job_id,
        )
        is None
    )


def test_delete_missing_job():
    service = ScanJobService()

    deleted = service.delete_job(
        "missing-job",
    )

    assert deleted is False


def test_cancel_existing_job():
    service = ScanJobService()

    job = service.create_job(
        "python",
        "cpython",
    )

    cancelled = service.cancel_job(
        job.job_id,
    )

    assert cancelled is job
    assert job.status == ScanStatus.CANCELLED


def test_cancel_missing_job():
    service = ScanJobService()

    cancelled = service.cancel_job(
        "missing",
    )

    assert cancelled is None


def test_find_jobs_no_filters():
    service = ScanJobService()

    first = service.create_job(
        "python",
        "cpython",
    )

    second = service.create_job(
        "fastapi",
        "fastapi",
    )

    jobs = service.find_jobs()

    assert len(jobs) == 2

    assert jobs[0] is second

    assert jobs[1] is first


def test_find_jobs_by_status():
    service = ScanJobService()

    service.create_job(
        "python",
        "cpython",
    )

    second = service.create_job(
        "fastapi",
        "fastapi",
    )

    second.status = ScanStatus.COMPLETED

    jobs = service.find_jobs(
        status=ScanStatus.COMPLETED,
    )

    assert jobs == [second]


def test_find_jobs_by_owner():
    service = ScanJobService()

    service.create_job(
        "python",
        "cpython",
    )

    second = service.create_job(
        "fastapi",
        "fastapi",
    )

    jobs = service.find_jobs(
        owner="fastapi",
    )

    assert jobs == [second]


def test_find_jobs_by_repository():
    service = ScanJobService()

    first = service.create_job(
        "python",
        "cpython",
    )

    service.create_job(
        "python",
        "django",
    )

    jobs = service.find_jobs(
        repository="cpython",
    )

    assert jobs == [first]


def test_cancel_queued_job():
    service = ScanJobService()

    job = service.create_job(
        "python",
        "cpython",
    )

    cancelled = service.cancel_job(
        job.job_id,
    )

    assert cancelled is job
    assert cancelled.status == ScanStatus.CANCELLED


def test_cancel_running_job():
    service = ScanJobService()

    job = service.create_job(
        "python",
        "cpython",
    )

    job.status = ScanStatus.RUNNING

    cancelled = service.cancel_job(
        job.job_id,
    )

    assert cancelled.status == ScanStatus.CANCELLED


def test_cancel_completed_job():
    service = ScanJobService()

    job = service.create_job(
        "python",
        "cpython",
    )

    job.status = ScanStatus.COMPLETED

    cancelled = service.cancel_job(
        job.job_id,
    )

    assert cancelled.status == ScanStatus.COMPLETED


def test_cancel_failed_job():
    service = ScanJobService()

    job = service.create_job(
        "python",
        "cpython",
    )

    job.status = ScanStatus.FAILED

    cancelled = service.cancel_job(
        job.job_id,
    )

    assert cancelled.status == ScanStatus.FAILED


def test_cancel_unknown_job():
    service = ScanJobService()

    assert (
        service.cancel_job(
            "missing",
        )
        is None
    )
