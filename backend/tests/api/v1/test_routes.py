from unittest.mock import AsyncMock, MagicMock

from fastapi import FastAPI
from fastapi.testclient import TestClient

from issuescout.api.v1.routes import (
    get_issue_service,
    get_repository_service,
    get_scan_job_service,
    get_scanner_engine,
    router,
)
from issuescout.models.scan_status import ScanStatus

app = FastAPI()
app.include_router(router)


def test_github_endpoint():
    service = AsyncMock()

    service.get_repository.return_value = {
        "name": "cpython",
        "owner": {
            "login": "python",
        },
        "stargazers_count": 100,
        "forks_count": 20,
        "open_issues_count": 30,
        "default_branch": "main",
    }

    app.dependency_overrides[get_repository_service] = lambda: service

    client = TestClient(app)

    response = client.get(
        "/github/python/cpython",
    )

    assert response.status_code == 200

    assert response.json() == {
        "name": "cpython",
        "owner": "python",
        "stars": 100,
        "forks": 20,
        "open_issues": 30,
        "default_branch": "main",
    }

    service.get_repository.assert_awaited_once_with(
        "python",
        "cpython",
    )

    service.close.assert_awaited_once()

    app.dependency_overrides.clear()


def test_issues_endpoint():
    service = AsyncMock()

    service.list_open_issues.return_value = [
        {
            "number": 1,
            "title": "Issue One",
            "assignee": {
                "login": "alice",
            },
        },
        {
            "number": 2,
            "title": "Issue Two",
            "assignee": None,
        },
    ]

    app.dependency_overrides[get_issue_service] = lambda: service

    client = TestClient(app)

    response = client.get(
        "/issues/python/cpython",
    )

    assert response.status_code == 200

    assert response.json() == [
        {
            "number": 1,
            "title": "Issue One",
            "assignee": "alice",
        },
        {
            "number": 2,
            "title": "Issue Two",
            "assignee": None,
        },
    ]

    service.list_open_issues.assert_awaited_once_with(
        "python",
        "cpython",
    )

    service.close.assert_awaited_once()

    app.dependency_overrides.clear()


def test_scan_repository_endpoint():
    engine = AsyncMock()

    engine.scan_repository.return_value = {
        "repository": "python/cpython",
        "total_issues": 5,
    }

    app.dependency_overrides[get_scanner_engine] = lambda: engine

    client = TestClient(app)

    response = client.get(
        "/scan/repository/python/cpython",
    )

    assert response.status_code == 200

    assert response.json() == {
        "repository": "python/cpython",
        "total_issues": 5,
    }

    engine.scan_repository.assert_awaited_once_with(
        "python",
        "cpython",
    )

    app.dependency_overrides.clear()


def test_create_scan_job():
    service = MagicMock()

    job = MagicMock()

    job.job_id = "job-123"

    job.status.value = "queued"

    service.create_job.return_value = job

    app.dependency_overrides[get_scan_job_service] = lambda: service

    client = TestClient(app)

    response = client.post(
        "/scan/python/cpython",
    )

    assert response.status_code == 200

    assert response.json() == {
        "job_id": "job-123",
        "status": "queued",
    }

    service.create_job.assert_called_once_with(
        "python",
        "cpython",
    )

    app.dependency_overrides.clear()


def test_scan_job_status():
    service = MagicMock()

    job = MagicMock()

    job.job_id = "job-123"

    job.status.value = "running"

    service.get_job_status.return_value = job

    app.dependency_overrides[get_scan_job_service] = lambda: service

    client = TestClient(app)

    job.progress = 45

    job.processed_issues = 9

    job.total_issues = 20

    response = client.get(
        "/scan/jobs/job-123",
    )

    assert response.status_code == 200

    assert response.json() == {
        "job_id": "job-123",
        "status": "running",
        "progress": 45,
        "processed_issues": 9,
        "total_issues": 20,
    }

    app.dependency_overrides.clear()


def test_scan_job_not_found():
    service = MagicMock()

    service.get_job_status.return_value = None

    app.dependency_overrides[get_scan_job_service] = lambda: service

    client = TestClient(app)

    response = client.get(
        "/scan/jobs/unknown",
    )

    assert response.status_code == 404

    app.dependency_overrides.clear()


def test_delete_scan_job():
    service = MagicMock()

    service.delete_job.return_value = True

    app.dependency_overrides[get_scan_job_service] = lambda: service

    client = TestClient(app)

    response = client.delete(
        "/scan/jobs/job-123",
    )

    assert response.status_code == 204

    service.delete_job.assert_called_once_with(
        "job-123",
    )

    app.dependency_overrides.clear()


def test_delete_scan_job_not_found():
    service = MagicMock()

    service.delete_job.return_value = False

    app.dependency_overrides[get_scan_job_service] = lambda: service

    client = TestClient(app)

    response = client.delete(
        "/scan/jobs/job-123",
    )

    assert response.status_code == 404

    app.dependency_overrides.clear()


def test_list_scan_jobs():
    service = MagicMock()

    job = MagicMock()

    job.job_id = "job-123"
    job.owner = "python"
    job.repository = "cpython"
    job.status.value = "running"
    job.progress = 50
    job.processed_issues = 5
    job.total_issues = 10

    service.find_jobs.return_value = [
        job,
    ]

    app.dependency_overrides[get_scan_job_service] = lambda: service

    client = TestClient(app)

    response = client.get(
        "/scan/jobs",
    )

    assert response.status_code == 200

    assert response.json() == [
        {
            "job_id": "job-123",
            "owner": "python",
            "repository": "cpython",
            "status": "running",
            "progress": 50,
            "processed_issues": 5,
            "total_issues": 10,
        }
    ]

    service.find_jobs.assert_called_once_with(
        status=None,
        owner=None,
        repository=None,
        limit=None,
        offset=0,
    )

    app.dependency_overrides.clear()


def test_list_scan_jobs_filter_status():
    service = MagicMock()

    service.find_jobs.return_value = []

    app.dependency_overrides[get_scan_job_service] = lambda: service

    client = TestClient(app)

    response = client.get(
        "/scan/jobs?status=completed",
    )

    assert response.status_code == 200

    service.find_jobs.assert_called_once()

    kwargs = service.find_jobs.call_args.kwargs

    assert kwargs["status"].value == "completed"
    assert kwargs["owner"] is None
    assert kwargs["repository"] is None

    app.dependency_overrides.clear()


def test_list_scan_jobs_filter_owner():
    service = MagicMock()

    service.find_jobs.return_value = []

    app.dependency_overrides[get_scan_job_service] = lambda: service

    client = TestClient(app)

    response = client.get(
        "/scan/jobs?owner=python",
    )

    assert response.status_code == 200

    service.find_jobs.assert_called_once_with(
        status=None,
        owner="python",
        repository=None,
        limit=None,
        offset=0,
    )

    app.dependency_overrides.clear()


def test_list_scan_jobs_filter_repository():
    service = MagicMock()

    service.find_jobs.return_value = []

    app.dependency_overrides[get_scan_job_service] = lambda: service

    client = TestClient(app)

    response = client.get(
        "/scan/jobs?repository=cpython",
    )

    assert response.status_code == 200

    service.find_jobs.assert_called_once_with(
        status=None,
        owner=None,
        repository="cpython",
        limit=None,
        offset=0,
    )

    app.dependency_overrides.clear()


def test_cancel_scan_job():
    service = MagicMock()

    job = MagicMock()
    job.job_id = "job-123"
    job.status = ScanStatus.CANCELLED
    job.progress = 0
    job.processed_issues = 0
    job.total_issues = 10

    service.cancel_job.return_value = job

    app.dependency_overrides[get_scan_job_service] = lambda: service

    client = TestClient(app)

    response = client.post(
        "/scan/jobs/job-123/cancel",
    )

    assert response.status_code == 200

    assert response.json() == {
        "job_id": "job-123",
        "status": "cancelled",
        "progress": 0,
        "processed_issues": 0,
        "total_issues": 10,
    }

    service.cancel_job.assert_called_once_with(
        "job-123",
    )

    app.dependency_overrides.clear()


def test_cancel_scan_job_not_found():
    service = MagicMock()

    service.cancel_job.return_value = None

    app.dependency_overrides[get_scan_job_service] = lambda: service

    client = TestClient(app)

    response = client.post(
        "/scan/jobs/job-123/cancel",
    )

    assert response.status_code == 404

    app.dependency_overrides.clear()


def test_cancel_completed_scan_job():
    service = MagicMock()

    job = MagicMock()
    job.status = ScanStatus.COMPLETED

    service.cancel_job.return_value = job

    app.dependency_overrides[get_scan_job_service] = lambda: service

    client = TestClient(app)

    response = client.post(
        "/scan/jobs/job-123/cancel",
    )

    assert response.status_code == 409

    app.dependency_overrides.clear()


def test_cancel_failed_scan_job():
    service = MagicMock()

    job = MagicMock()
    job.status = ScanStatus.FAILED

    service.cancel_job.return_value = job

    app.dependency_overrides[get_scan_job_service] = lambda: service

    client = TestClient(app)

    response = client.post(
        "/scan/jobs/job-123/cancel",
    )

    assert response.status_code == 409

    app.dependency_overrides.clear()
