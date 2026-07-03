from unittest.mock import AsyncMock

import pytest

from issuescout.github.comments import CommentAPI


@pytest.mark.anyio
async def test_list_comments():
    api = CommentAPI()

    api.client.get_all = AsyncMock(
        return_value=[{"id": 1}],
    )

    result = await api.list(
        "owner",
        "repo",
        15,
    )

    api.client.get_all.assert_awaited_once_with(
        "/repos/owner/repo/issues/15/comments",
    )

    assert result[0]["id"] == 1


@pytest.mark.anyio
async def test_close():
    api = CommentAPI()

    api.client.close = AsyncMock()

    await api.close()

    api.client.close.assert_awaited_once()
