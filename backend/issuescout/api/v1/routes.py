from fastapi import APIRouter

from issuescout.services.issue_service import IssueService
from issuescout.services.repository_service import RepositoryService
from issuescout.scanner.engine import ScannerEngine

router = APIRouter()


@router.get("/github")
async def github():
    service = RepositoryService()

    repo = await service.get_repository(
        "python",
        "cpython",
    )

    await service.close()

    return {
        "name": repo["name"],
        "owner": repo["owner"]["login"],
        "stars": repo["stargazers_count"],
        "forks": repo["forks_count"],
        "open_issues": repo["open_issues_count"],
        "default_branch": repo["default_branch"],
    }


@router.get("/issues")
async def issues():
    service = IssueService()

    issues = await service.list_open_issues(
        "python",
        "cpython",
    )

    await service.close()

    return [
        {
            "number": issue["number"],
            "title": issue["title"],
            "assignee": (
                issue["assignee"]["login"]
                if issue["assignee"]
                else None
            ),
        }
        for issue in issues
    ]

@router.get("/scan/{owner}/{repo}")
async def scan_repository(
    owner: str,
    repo: str,
):
    engine = ScannerEngine()

    return await engine.scan_repository(owner, repo)