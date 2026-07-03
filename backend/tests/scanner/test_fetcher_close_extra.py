import asyncio

from issuescout.scanner.fetcher import Fetcher


class FakeService:
    def __init__(self):
        self.closed = False

    async def close(self):
        self.closed = True


def test_close():
    fetcher = Fetcher()

    fetcher.issue_service = FakeService()
    fetcher.repository_service = FakeService()
    fetcher.pull_request_service = FakeService()
    fetcher.review_service = FakeService()
    fetcher.commit_history_service = FakeService()

    asyncio.run(fetcher.close())

    assert fetcher.issue_service.closed
    assert fetcher.repository_service.closed
    assert fetcher.pull_request_service.closed
    assert fetcher.review_service.closed
    assert fetcher.commit_history_service.closed
