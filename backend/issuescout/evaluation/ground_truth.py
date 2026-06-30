from __future__ import annotations

from issuescout.evaluation.models import GroundTruthRecord
from issuescout.github.client import GitHubClient


class GroundTruthCollector:
    """
    Collects verified Issue → Pull Request relationships from GitHub.

    The collector is repository-agnostic and is intended to work for any
    GitHub repository supported by IssueScout.
    """

    def __init__(self) -> None:
        self.client = GitHubClient()

    async def collect(
        self,
        owner: str,
        repository: str,
        issue_number: int,
    ) -> GroundTruthRecord:
        """
        Collect one verified ground-truth record.

        This is currently a placeholder implementation.

        A future implementation will inspect GitHub timeline events,
        cross references and closing events to determine which pull
        request actually resolved the issue.
        """

        return GroundTruthRecord(
            repository_owner=owner,
            repository_name=repository,
            issue_number=issue_number,
            issue_title="",
            issue_state="closed",
            actual_pull_request=None,
            linkage_method="unimplemented",
        )

    async def close(self) -> None:
        await self.client.close()
