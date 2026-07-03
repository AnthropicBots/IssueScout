from unittest.mock import AsyncMock

import pytest

from issuescout.github.pulls import PullRequestAPI


@pytest.mark.anyio
async def test_get_pull_request():
    api = PullRequestAPI()

    api.client.get = AsyncMock(
        return_value={"number": 5},
    )

    result = await api.get(
        "owner",
        "repo",
        5,
    )

    api.client.get.assert_awaited_once_with(
        "/repos/owner/repo/pulls/5",
    )

    assert result["number"] == 5


@pytest.mark.anyio
async def test_close():
    api = PullRequestAPI()

    api.client.close = AsyncMock()

    await api.close()

    api.client.close.assert_awaited_once()
