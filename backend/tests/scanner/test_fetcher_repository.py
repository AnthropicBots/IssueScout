import asyncio

from issuescout.scanner.fetcher import Fetcher


class FakeRepositoryService:
    async def get_repository(
        self,
        owner,
        repo,
    ):
        return {
            "owner": {
                "login": owner,
            },
            "name": repo,
        }


def test_fetch_repository():
    fetcher = Fetcher()

    fetcher.repository_service = FakeRepositoryService()

    repository = asyncio.run(
        fetcher.fetch_repository(
            "owner",
            "repo",
        )
    )

    assert repository["name"] == "repo"
    assert repository["owner"]["login"] == "owner"
