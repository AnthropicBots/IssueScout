from __future__ import annotations

from issuescout.github.client import GitHubClient


class IssueAPI:
    """
    GitHub Issue API wrapper.
    """

    def __init__(self) -> None:
        self.client = GitHubClient()

    async def get_issue(
        self,
        owner: str,
        repository: str,
        issue_number: int,
    ):
        return await self.client.get(
            f"/repos/{owner}/{repository}/issues/{issue_number}"
        )

    async def list_closed(
        self,
        owner: str,
        repository: str,
        limit: int = 100,
    ):
        return await self.client.get_all(
            (f"/repos/{owner}/{repository}/issues?state=closed&per_page={limit}")
        )

    async def close(self):
        await self.client.close()
