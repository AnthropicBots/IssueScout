import asyncio

from issuescout.scanner.fetcher import Fetcher


class FakeCommitHistoryService:
    async def list_branch_commits(
        self,
        owner,
        repo,
        branch,
    ):
        return [
            "commit-1",
            "commit-2",
        ]


def test_commit_history_service():
    fetcher = Fetcher()

    fetcher.commit_history_service = FakeCommitHistoryService()

    commits = asyncio.run(
        fetcher.commit_history_service.list_branch_commits(
            "owner",
            "repo",
            "main",
        )
    )

    assert commits == [
        "commit-1",
        "commit-2",
    ]
