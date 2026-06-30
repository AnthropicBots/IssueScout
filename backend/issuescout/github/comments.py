from __future__ import annotations

from issuescout.github.client import GitHubClient


class CommentAPI:
    """
    GitHub Issue Comment API wrapper.
    """

    def __init__(self) -> None:
        self.client = GitHubClient()

    async def list(
        self,
        owner: str,
        repository: str,
        issue_number: int,
    ):
        return await self.client.get_all(
            (f"/repos/{owner}/{repository}/issues/{issue_number}/comments")
        )

    async def close(self):
        await self.client.close()
