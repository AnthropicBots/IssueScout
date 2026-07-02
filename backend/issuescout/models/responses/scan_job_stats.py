from pydantic import BaseModel


class ScanJobStatsResponse(BaseModel):
    """
    Summary statistics for repository scan jobs.
    """

    total_jobs: int

    queued_jobs: int

    running_jobs: int

    completed_jobs: int

    failed_jobs: int
