from unittest.mock import AsyncMock

import pytest

from issuescout.application.scan_service import (
    ApplicationScanService,
)


@pytest.mark.anyio
async def test_scan_repository():
    scanner = AsyncMock()

    scanner.scan_repository.return_value = "result"

    service = ApplicationScanService(
        scanner,
    )

    result = await service.scan_repository(
        "owner",
        "repo",
    )

    assert result == "result"

    scanner.scan_repository.assert_awaited_once_with(
        "owner",
        "repo",
    )
