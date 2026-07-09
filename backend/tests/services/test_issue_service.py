from unittest.mock import AsyncMock, patch

import pytest

from issuescout.services.issue_service import IssueService

pytestmark = pytest.mark.anyio


async def test_get_issue():

    with patch(
        "issuescout.services.issue_service.IssueAPI",
    ) as MockAPI:
        api = MockAPI.return_value

        api.get_issue = AsyncMock(
            return_value={
                "number": 123,
                "title": "Example Issue",
            }
        )

        service = IssueService()

        result = await service.get_issue(
            "python",
            "cpython",
            123,
        )

        assert result["number"] == 123

        api.get_issue.assert_awaited_once_with(
            "python",
            "cpython",
            123,
        )


async def test_list_open_issues():

    with patch(
        "issuescout.services.issue_service.IssueAPI",
    ) as MockAPI:
        api = MockAPI.return_value

        api.list_open = AsyncMock(
            return_value=[
                {
                    "number": 1,
                },
            ]
        )

        service = IssueService()

        result = await service.list_open_issues(
            "python",
            "cpython",
        )

        assert result == [
            {
                "number": 1,
            }
        ]

        api.list_open.assert_awaited_once_with(
            "python",
            "cpython",
        )


async def test_list_closed_issues():

    with patch(
        "issuescout.services.issue_service.IssueAPI",
    ) as MockAPI:
        api = MockAPI.return_value

        api.list_closed = AsyncMock(
            return_value=[
                {
                    "number": 10,
                },
            ]
        )

        service = IssueService()

        result = await service.list_closed_issues(
            "python",
            "cpython",
        )

        assert result == [
            {
                "number": 10,
            }
        ]

        api.list_closed.assert_awaited_once_with(
            "python",
            "cpython",
            limit=100,
        )


async def test_close():

    with patch(
        "issuescout.services.issue_service.IssueAPI",
    ) as MockAPI:
        api = MockAPI.return_value

        api.close = AsyncMock()

        service = IssueService()

        await service.close()

        api.close.assert_awaited_once()


async def test_list_open_issues_with_limit():

    with patch(
        "issuescout.services.issue_service.IssueAPI",
    ) as MockAPI:
        api = MockAPI.return_value

        api.list_open = AsyncMock(
            return_value=[],
        )

        service = IssueService()

        await service.list_open_issues(
            "python",
            "cpython",
            limit=25,
        )

        api.list_open.assert_awaited_once_with(
            "python",
            "cpython",
            limit=25,
        )


async def test_list_open_issues_with_page_size():

    with patch(
        "issuescout.services.issue_service.IssueAPI",
    ) as MockAPI:
        api = MockAPI.return_value

        api.list_open = AsyncMock(
            return_value=[],
        )

        service = IssueService()

        await service.list_open_issues(
            "python",
            "cpython",
            page_size=50,
        )

        api.list_open.assert_awaited_once_with(
            "python",
            "cpython",
            page_size=50,
        )


async def test_list_open_issues_with_limit_and_page_size():

    with patch(
        "issuescout.services.issue_service.IssueAPI",
    ) as MockAPI:
        api = MockAPI.return_value

        api.list_open = AsyncMock(
            return_value=[],
        )

        service = IssueService()

        await service.list_open_issues(
            "python",
            "cpython",
            limit=25,
            page_size=50,
        )

        api.list_open.assert_awaited_once_with(
            "python",
            "cpython",
            limit=25,
            page_size=50,
        )


async def test_list_closed_issues_custom_limit():

    with patch(
        "issuescout.services.issue_service.IssueAPI",
    ) as MockAPI:
        api = MockAPI.return_value

        api.list_closed = AsyncMock(
            return_value=[],
        )

        service = IssueService()

        await service.list_closed_issues(
            "python",
            "cpython",
            limit=5,
        )

        api.list_closed.assert_awaited_once_with(
            "python",
            "cpython",
            limit=5,
        )
