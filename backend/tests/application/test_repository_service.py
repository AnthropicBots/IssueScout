from unittest.mock import AsyncMock

import pytest

from issuescout.application.repository_service import (
    ApplicationRepositoryService,
)


@pytest.mark.anyio
async def test_get_repository():

    service = AsyncMock()

    service.get_repository.return_value = {
        "name": "IssueScout",
    }

    app = ApplicationRepositoryService(
        service=service,
    )

    result = await app.get_repository(
        "owner",
        "repo",
    )

    assert result["name"] == "IssueScout"

    service.get_repository.assert_awaited_once_with(
        "owner",
        "repo",
    )


@pytest.mark.anyio
async def test_close():

    service = AsyncMock()

    app = ApplicationRepositoryService(
        service=service,
    )

    await app.close()

    service.close.assert_awaited_once()


@pytest.mark.anyio
async def test_get_repository_propagates_exception():

    service = AsyncMock()

    service.get_repository.side_effect = RuntimeError("boom")

    app = ApplicationRepositoryService(
        service=service,
    )

    with pytest.raises(RuntimeError):
        await app.get_repository(
            "owner",
            "repo",
        )
