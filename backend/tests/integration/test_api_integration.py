from fastapi.testclient import TestClient

from issuescout.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    print(response.json())

    assert response.status_code == 200


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"


def test_unknown_route_returns_404():
    response = client.get("/this-route-does-not-exist")

    assert response.status_code == 404


def test_scan_job_statistics_endpoint():
    response = client.get("/api/v1/scan/jobs/stats")

    assert response.status_code == 200

    data = response.json()

    assert "total_jobs" in data
    assert "queued_jobs" in data
    assert "running_jobs" in data
    assert "completed_jobs" in data
    assert "failed_jobs" in data


def test_list_scan_jobs_endpoint():
    response = client.get("/api/v1/scan/jobs")

    assert response.status_code == 200

    assert isinstance(response.json(), list)
