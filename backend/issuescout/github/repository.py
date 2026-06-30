from __future__ import annotations

from issuescout.github.client import GitHubClient


class RepositoryAPI:
    """
    GitHub Repository API wrapper.
    """

    def __init__(self) -> None:
        self.client = GitHubClient()

    async def get(
        self,
        owner: str,
        repository: str,
    ):
        return await self.client.get(f"/repos/{owner}/{repository}")

    async def close(self):
        await self.client.close()
