from __future__ import annotations

from issuescout.github.client import GitHubClient


class PullRequestAPI:
    """
    GitHub Pull Request API wrapper.
    """

    def __init__(self) -> None:
        self.client = GitHubClient()

    async def get(
        self,
        owner: str,
        repository: str,
        pull_request: int,
    ):
        return await self.client.get(
            (f"/repos/{owner}/{repository}/pulls/{pull_request}")
        )

    async def close(self):
        await self.client.close()
