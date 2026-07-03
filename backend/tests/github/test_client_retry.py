import pytest
import httpx

from issuescout.core.exceptions import GitHubAPIError
from issuescout.github.client import GitHubClient


@pytest.mark.anyio
async def test_retry_exhaustion(monkeypatch):
    client = GitHubClient()

    async def failing_get(*args, **kwargs):
        raise httpx.ConnectError("boom")

    monkeypatch.setattr(
        client.client,
        "get",
        failing_get,
    )

    with pytest.raises(GitHubAPIError):
        await client.get("/repos/test/test")

    await client.close()
