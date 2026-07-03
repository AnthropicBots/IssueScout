"""
Reusable OpenAPI examples.
"""

REPOSITORY_EXAMPLE = {
    "name": "angular",
    "owner": "angular",
    "stars": 100000,
    "forks": 27000,
    "open_issues": 2500,
    "default_branch": "main",
}

SCAN_JOB_STATS_EXAMPLE = {
    "total": 12,
    "queued": 2,
    "running": 1,
    "completed": 8,
    "failed": 1,
}

SCAN_JOB_CREATED_EXAMPLE = {
    "job_id": "scan_123456789",
    "status": "queued",
}

HEALTH_EXAMPLE = {
    "status": "healthy",
    "service": "IssueScout API",
    "version": "0.1.0",
}
