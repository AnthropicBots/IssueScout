from typing import Annotated

from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
    HTTPException,
    Query,
    status,
)
from issuescout.models.responses import (
    IssueResponse,
    RepositoryResponse,
    ScanJobResponse,
    ScanJobResultResponse,
    ScanJobStatsResponse,
    ScanJobStatusResponse,
    ScanJobSummaryResponse,
)
from issuescout.scanner.engine import ScannerEngine
from issuescout.models.scan_status import ScanStatus
from issuescout.services.issue_service import IssueService
from issuescout.services.repository_service import RepositoryService
from issuescout.services.scan_job_service import ScanJobService

router = APIRouter(
    tags=["GitHub"],
)
scan_job_service = ScanJobService()


def get_repository_service() -> RepositoryService:
    return RepositoryService()


def get_issue_service() -> IssueService:
    return IssueService()


def get_scanner_engine() -> ScannerEngine:
    return ScannerEngine()


def get_scan_job_service() -> ScanJobService:
    return scan_job_service


@router.get(
    "/github/{owner}/{repository}",
    response_model=RepositoryResponse,
    summary="Repository Information",
    description="Retrieve metadata for any GitHub repository.",
)
async def github(
    owner: str,
    repository: str,
    service: RepositoryService = Depends(
        get_repository_service,
    ),
):
    repo = await service.get_repository(
        owner,
        repository,
    )

    await service.close()

    return RepositoryResponse(
        name=repo["name"],
        owner=repo["owner"]["login"],
        stars=repo["stargazers_count"],
        forks=repo["forks_count"],
        open_issues=repo["open_issues_count"],
        default_branch=repo["default_branch"],
    )


@router.get(
    "/issues/{owner}/{repository}",
    response_model=list[IssueResponse],
    summary="List Open Issues",
    description="Retrieve all currently open issues for any GitHub repository.",
)
async def issues(
    owner: str,
    repository: str,
    service: IssueService = Depends(
        get_issue_service,
    ),
):
    issues = await service.list_open_issues(
        owner,
        repository,
    )

    await service.close()

    return [
        IssueResponse(
            number=issue["number"],
            title=issue["title"],
            assignee=(issue["assignee"]["login"] if issue["assignee"] else None),
        )
        for issue in issues
    ]


@router.post(
    "/scan/{owner}/{repository}",
    response_model=ScanJobResponse,
    summary="Create Scan Job",
    description="Create a repository scan job.",
)
async def create_scan_job(
    owner: str,
    repository: str,
    background_tasks: BackgroundTasks,
    service: ScanJobService = Depends(
        get_scan_job_service,
    ),
):
    job = service.create_job(
        owner,
        repository,
    )

    background_tasks.add_task(
        service.run_job,
        job,
    )

    return ScanJobResponse(
        job_id=job.job_id,
        status=job.status.value,
    )


@router.get(
    "/scan/jobs",
    response_model=list[ScanJobSummaryResponse],
    summary="List Scan Jobs",
)
async def list_scan_jobs(
    status: str | None = None,
    owner: str | None = None,
    repository: str | None = None,
    limit: Annotated[
        int | None,
        Query(
            ge=1,
            le=100,
        ),
    ] = None,
    offset: Annotated[
        int,
        Query(
            ge=0,
        ),
    ] = 0,
    service: ScanJobService = Depends(
        get_scan_job_service,
    ),
):
    scan_status = ScanStatus(status) if status is not None else None

    jobs = service.find_jobs(
        status=scan_status,
        owner=owner,
        repository=repository,
        limit=limit,
        offset=offset,
    )

    return [
        ScanJobSummaryResponse(
            job_id=job.job_id,
            owner=job.owner,
            repository=job.repository,
            status=job.status.value,
            progress=job.progress,
            processed_issues=job.processed_issues,
            total_issues=job.total_issues,
        )
        for job in jobs
    ]


@router.get(
    "/scan/jobs/stats",
    response_model=ScanJobStatsResponse,
    summary="Scan Job Statistics",
)
async def get_scan_job_statistics(
    service: ScanJobService = Depends(
        get_scan_job_service,
    ),
):
    return ScanJobStatsResponse(
        **service.get_statistics(),
    )


@router.get(
    "/scan/jobs/{job_id}",
    response_model=ScanJobStatusResponse,
    summary="Get Scan Job Status",
)
async def get_scan_job_status(
    job_id: str,
    service: ScanJobService = Depends(
        get_scan_job_service,
    ),
):
    job = service.get_job_status(job_id)

    if job is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Scan job not found.",
        )

    return ScanJobStatusResponse(
        job_id=job.job_id,
        status=job.status.value,
        progress=job.progress,
        processed_issues=job.processed_issues,
        total_issues=job.total_issues,
    )


@router.get(
    "/scan/jobs/{job_id}/result",
    response_model=ScanJobResultResponse,
    summary="Get Scan Result",
)
async def get_scan_job_result(
    job_id: str,
    service: ScanJobService = Depends(
        get_scan_job_service,
    ),
):
    job = service.get_job_result(job_id)

    if job is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Scan job not found.",
        )

    if job.result is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Scan has not completed yet.",
        )

    return job.result


@router.post(
    "/scan/jobs/{job_id}/cancel",
    response_model=ScanJobStatusResponse,
    summary="Cancel Scan Job",
)
async def cancel_scan_job(
    job_id: str,
    service: ScanJobService = Depends(
        get_scan_job_service,
    ),
):
    job = service.cancel_job(
        job_id,
    )

    if job is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Scan job not found.",
        )

    if job.status != ScanStatus.CANCELLED:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Scan job cannot be cancelled.",
        )

    return ScanJobStatusResponse(
        job_id=job.job_id,
        status=job.status.value,
        progress=job.progress,
        processed_issues=job.processed_issues,
        total_issues=job.total_issues,
    )


@router.delete(
    "/scan/jobs/{job_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete Scan Job",
)
async def delete_scan_job(
    job_id: str,
    service: ScanJobService = Depends(
        get_scan_job_service,
    ),
):
    deleted = service.delete_job(
        job_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Scan job not found.",
        )


@router.get(
    "/scan/repository/{owner}/{repository}",
    summary="Scan Repository",
    description=(
        "Synchronously analyze a GitHub repository and "
        "predict pull request relationships for open issues."
    ),
)
async def scan_repository(
    owner: str,
    repository: str,
    engine: ScannerEngine = Depends(
        get_scanner_engine,
    ),
):
    return await engine.scan_repository(
        owner,
        repository,
    )
