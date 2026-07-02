from pydantic import BaseModel


class ScanJobResponse(BaseModel):
    """
    Response returned when a scan job is created.
    """

    job_id: str

    status: str


class ScanJobStatusResponse(BaseModel):
    job_id: str

    status: str

    progress: int

    processed_issues: int

    total_issues: int


class ScanJobSummaryResponse(BaseModel):
    """
    Summary information for a scan job.
    """

    job_id: str

    owner: str

    repository: str

    status: str

    progress: int

    processed_issues: int

    total_issues: int


class ScanJobResultResponse(BaseModel):
    """
    Result of a completed scan job.
    """

    repository: str

    total_issues: int
