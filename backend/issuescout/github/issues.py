from __future__ import annotations

from issuescout.github.client import GitHubClient


class IssueAPI:
    """
    GitHub Issue REST API wrapper.
    """

    def __init__(self) -> None:
        self.client = GitHubClient()

    async def get_issue(
        self,
        owner: str,
        repository: str,
        issue_number: int,
    ) -> dict:
        """
        Retrieve a single GitHub issue.
        """
        return await self.client.get(
            f"/repos/{owner}/{repository}/issues/{issue_number}"
        )

    async def list_open(
        self,
        owner: str,
        repository: str,
        *,
        limit: int | None = 100,
        page_size: int | None = None,
    ) -> list[dict]:
        """
        Retrieve open issues.

        Supports incremental scanning by limiting
        the number of retrieved issues.
        """

        if page_size is None:
            return await self.client.get_all(
                f"/repos/{owner}/{repository}/issues?state=open",
                limit=limit,
            )

        return await self.client.get_all(
            f"/repos/{owner}/{repository}/issues?state=open",
            limit=limit,
            page_size=page_size,
        )

    async def list_closed(
        self,
        owner: str,
        repository: str,
        *,
        limit: int | None = 100,
        page_size: int | None = None,
    ) -> list[dict]:
        """
        Retrieve closed issues.
        """

        if page_size is None:
            return await self.client.get_all(
                f"/repos/{owner}/{repository}/issues?state=closed",
                limit=limit,
            )

        return await self.client.get_all(
            f"/repos/{owner}/{repository}/issues?state=closed",
            limit=limit,
            page_size=page_size,
        )

    async def close(self) -> None:
        """
        Close the GitHub client.
        """
        await self.client.close()
