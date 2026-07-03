from typing import Annotated

from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
    HTTPException,
    Query,
    status,
)

from issuescout.api.v1.dependencies import (
    get_issue_service,
    get_repository_service,
    get_scan_job_service,
    get_scanner_engine,
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
from issuescout.application.repository_service import (
    ApplicationRepositoryService,
)
from issuescout.services.scan_job_service import ScanJobService
from issuescout.api.v1.docs.responses import (
    REPOSITORY_RESPONSES,
    SCAN_JOB_CREATE_RESPONSES,
    SCAN_JOB_STATS_RESPONSES,
)

from issuescout.api.v1.docs.summaries import (
    REPOSITORY_SUMMARY,
    ISSUES_SUMMARY,
    SCAN_CREATE_SUMMARY,
    SCAN_LIST_SUMMARY,
    SCAN_STATS_SUMMARY,
    SCAN_STATUS_SUMMARY,
    SCAN_RESULT_SUMMARY,
    SCAN_CANCEL_SUMMARY,
    SCAN_DELETE_SUMMARY,
    SYNC_SCAN_SUMMARY,
)

from issuescout.api.v1.docs.descriptions import (
    REPOSITORY_DESCRIPTION,
    ISSUES_DESCRIPTION,
    SCAN_CREATE_DESCRIPTION,
    SCAN_LIST_DESCRIPTION,
    SCAN_STATS_DESCRIPTION,
    SCAN_STATUS_DESCRIPTION,
    SCAN_RESULT_DESCRIPTION,
    SCAN_CANCEL_DESCRIPTION,
    SCAN_DELETE_DESCRIPTION,
    SYNC_SCAN_DESCRIPTION,
)

from issuescout.api.v1.docs.tags import (
    GITHUB_TAG,
)

router = APIRouter(
    tags=[str(GITHUB_TAG)],
)


@router.get(
    "/github/{owner}/{repository}",
    response_model=RepositoryResponse,
    summary=REPOSITORY_SUMMARY,
    description=REPOSITORY_DESCRIPTION,
    operation_id="getRepository",
    responses=REPOSITORY_RESPONSES,  # type: ignore[arg-type]
)
async def github(
    owner: str,
    repository: str,
    service: ApplicationRepositoryService = Depends(
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
    summary=ISSUES_SUMMARY,
    description=ISSUES_DESCRIPTION,
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
    summary=SCAN_CREATE_SUMMARY,
    description=SCAN_CREATE_DESCRIPTION,
    operation_id="createScanJob",
    responses=SCAN_JOB_CREATE_RESPONSES,  # type: ignore[arg-type]
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
    summary=SCAN_LIST_SUMMARY,
    description=SCAN_LIST_DESCRIPTION,
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
    summary=SCAN_STATS_SUMMARY,
    description=SCAN_STATS_DESCRIPTION,
    operation_id="getScanJobStatistics",
    responses=SCAN_JOB_STATS_RESPONSES,  # type: ignore[arg-type]
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
    summary=SCAN_STATUS_SUMMARY,
    description=SCAN_STATUS_DESCRIPTION,
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
    summary=SCAN_RESULT_SUMMARY,
    description=SCAN_RESULT_DESCRIPTION,
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
    summary=SCAN_CANCEL_SUMMARY,
    description=SCAN_CANCEL_DESCRIPTION,
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
    summary=SCAN_DELETE_SUMMARY,
    description=SCAN_DELETE_DESCRIPTION,
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
    summary=SYNC_SCAN_SUMMARY,
    description=SYNC_SCAN_DESCRIPTION,
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
