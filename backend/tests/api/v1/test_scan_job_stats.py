from fastapi import FastAPI
from fastapi.testclient import TestClient

from issuescout.api.v1.routes import (
    get_scan_job_service,
    router,
)
from issuescout.models.scan_status import ScanStatus
from issuescout.services.scan_job_service import ScanJobService

app = FastAPI()
app.include_router(router)

client = TestClient(app)


def test_scan_job_statistics_endpoint():
    service = ScanJobService()

    service.create_job(
        "python",
        "cpython",
    )

    running = service.create_job(
        "psf",
        "requests",
    )
    running.status = ScanStatus.RUNNING

    completed = service.create_job(
        "encode",
        "httpx",
    )
    completed.status = ScanStatus.COMPLETED

    failed = service.create_job(
        "tiangolo",
        "fastapi",
    )
    failed.status = ScanStatus.FAILED

    app.dependency_overrides[get_scan_job_service] = lambda: service

    response = client.get(
        "/scan/jobs/stats",
    )

    app.dependency_overrides.clear()

    assert response.status_code == 200

    assert response.json() == {
        "total_jobs": 4,
        "queued_jobs": 1,
        "running_jobs": 1,
        "completed_jobs": 1,
        "failed_jobs": 1,
    }


def test_scan_job_statistics_empty():
    service = ScanJobService()

    app.dependency_overrides[get_scan_job_service] = lambda: service

    response = client.get(
        "/scan/jobs/stats",
    )

    app.dependency_overrides.clear()

    assert response.status_code == 200

    assert response.json() == {
        "total_jobs": 0,
        "queued_jobs": 0,
        "running_jobs": 0,
        "completed_jobs": 0,
        "failed_jobs": 0,
    }
