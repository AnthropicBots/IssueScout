from unittest.mock import AsyncMock

import pytest

from issuescout.github.issues import IssueAPI


@pytest.mark.anyio
async def test_get_issue():
    api = IssueAPI()

    api.client.get = AsyncMock(
        return_value={"number": 10},
    )

    result = await api.get_issue(
        "owner",
        "repo",
        10,
    )

    api.client.get.assert_awaited_once_with(
        "/repos/owner/repo/issues/10",
    )

    assert result["number"] == 10


@pytest.mark.anyio
async def test_list_open():
    api = IssueAPI()

    api.client.get_all = AsyncMock(
        return_value=[{"number": 1}],
    )

    result = await api.list_open(
        "owner",
        "repo",
    )

    api.client.get_all.assert_awaited_once_with(
        "/repos/owner/repo/issues?state=open",
        limit=100,
    )

    assert len(result) == 1


@pytest.mark.anyio
async def test_list_closed():
    api = IssueAPI()

    api.client.get_all = AsyncMock(
        return_value=[{"number": 2}],
    )

    result = await api.list_closed(
        "owner",
        "repo",
    )

    api.client.get_all.assert_awaited_once_with(
        "/repos/owner/repo/issues?state=closed",
        limit=100,
    )

    assert len(result) == 1


@pytest.mark.anyio
async def test_close():
    api = IssueAPI()

    api.client.close = AsyncMock()

    await api.close()

    api.client.close.assert_awaited_once()
