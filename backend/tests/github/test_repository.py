from unittest.mock import AsyncMock

import pytest

from issuescout.github.repository import RepositoryAPI


@pytest.mark.anyio
async def test_get_repository():
    api = RepositoryAPI()

    api.client.get = AsyncMock(
        return_value={"name": "repo"},
    )

    result = await api.get(
        "owner",
        "repo",
    )

    api.client.get.assert_awaited_once_with(
        "/repos/owner/repo",
    )

    assert result["name"] == "repo"


@pytest.mark.anyio
async def test_close():
    api = RepositoryAPI()

    api.client.close = AsyncMock()

    await api.close()

    api.client.close.assert_awaited_once()
