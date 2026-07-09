from unittest.mock import AsyncMock

import pytest

from issuescout.application.candidate_pull_request_service import (
    CandidatePullRequestService,
)


@pytest.mark.anyio
async def test_discovers_from_multiple_sources():

    service = CandidatePullRequestService()

    service.issue_service.get_issue = AsyncMock(
        return_value={"body": ("https://github.com/angular/angular/pull/69607")}
    )

    service.comment_service.get_comments = AsyncMock(
        return_value=[{"body": ("See https://github.com/angular/angular/pull/69608")}]
    )

    service.timeline_service.get_issue_timeline = AsyncMock(
        return_value=[
            {
                "event": "cross-referenced",
                "body": ("https://github.com/angular/angular/pull/69607"),
            }
        ]
    )

    results = await service.discover(
        "angular",
        "angular",
        69603,
    )

    assert len(results) == 2

    assert results[0].number == 69607
    assert "body" in results[0].sources
    assert "timeline" in results[0].sources

    assert results[1].number == 69608
    assert "comment" in results[1].sources


@pytest.mark.anyio
async def test_returns_empty_when_no_references_exist():

    service = CandidatePullRequestService()

    service.issue_service.get_issue = AsyncMock(return_value={"body": ""})

    service.comment_service.get_comments = AsyncMock(return_value=[])

    service.timeline_service.get_issue_timeline = AsyncMock(return_value=[])

    results = await service.discover(
        "angular",
        "angular",
        1,
    )

    assert results == []


@pytest.mark.anyio
async def test_discovers_backport_reference():

    service = CandidatePullRequestService()

    service.issue_service.get_issue = AsyncMock(
        return_value={"body": "Backport #69607"}
    )

    service.comment_service.get_comments = AsyncMock(return_value=[])

    service.timeline_service.get_issue_timeline = AsyncMock(return_value=[])

    results = await service.discover(
        "angular",
        "angular",
        69603,
    )

    assert len(results) == 1
    assert results[0].number == 69607


@pytest.mark.anyio
async def test_discovers_pull_request_from_timeline_source():

    service = CandidatePullRequestService()

    service.issue_service.get_issue = AsyncMock(
        return_value={
            "body": "",
        }
    )

    service.comment_service.get_comments = AsyncMock(
        return_value=[],
    )

    service.timeline_service.get_issue_timeline = AsyncMock(
        return_value=[
            {
                "event": "cross-referenced",
                "source": {
                    "issue": {
                        "number": 69607,
                        "pull_request": {
                            "url": (
                                "https://api.github.com/"
                                "repos/angular/angular/pulls/69607"
                            )
                        },
                    }
                },
            }
        ]
    )

    results = await service.discover(
        "angular",
        "angular",
        69603,
    )

    assert len(results) == 1

    assert results[0].number == 69607

    assert "timeline" in results[0].sources


@pytest.mark.anyio
async def test_existing_numbers_are_filtered():

    service = CandidatePullRequestService()

    service.issue_service.get_issue = AsyncMock(
        return_value={
            "body": (
                "https://github.com/angular/angular/pull/69607\n"
                "https://github.com/angular/angular/pull/69608"
            ),
        }
    )

    service.comment_service.get_comments = AsyncMock(
        return_value=[],
    )

    service.timeline_service.get_issue_timeline = AsyncMock(
        return_value=[],
    )

    results = await service.discover(
        "angular",
        "angular",
        1,
        existing_numbers={69607},
    )

    assert len(results) == 1

    assert results[0].number == 69608


@pytest.mark.anyio
async def test_duplicate_references_are_merged():

    service = CandidatePullRequestService()

    service.issue_service.get_issue = AsyncMock(
        return_value={
            "body": ("https://github.com/angular/angular/pull/69607"),
        }
    )

    service.comment_service.get_comments = AsyncMock(
        return_value=[
            {
                "body": ("https://github.com/angular/angular/pull/69607"),
            }
        ],
    )

    service.timeline_service.get_issue_timeline = AsyncMock(
        return_value=[
            {
                "body": ("https://github.com/angular/angular/pull/69607"),
            }
        ],
    )

    results = await service.discover(
        "angular",
        "angular",
        1,
    )

    assert len(results) == 1

    assert results[0].number == 69607

    assert results[0].sources == {
        "body",
        "comment",
        "timeline",
    }


@pytest.mark.anyio
async def test_invalid_timeline_structure_is_ignored():

    service = CandidatePullRequestService()

    service.issue_service.get_issue = AsyncMock(
        return_value={
            "body": "",
        }
    )

    service.comment_service.get_comments = AsyncMock(
        return_value=[],
    )

    service.timeline_service.get_issue_timeline = AsyncMock(
        return_value=[
            {
                "source": None,
            },
            {
                "source": {},
            },
            {
                "source": {
                    "issue": {},
                },
            },
            {
                "source": {
                    "issue": {
                        "pull_request": {},
                    },
                },
            },
        ],
    )

    results = await service.discover(
        "angular",
        "angular",
        1,
    )

    assert results == []


@pytest.mark.anyio
async def test_close_closes_all_services():

    service = CandidatePullRequestService()

    service.issue_service.close = AsyncMock()

    service.comment_service.close = AsyncMock()

    service.timeline_service.close = AsyncMock()

    await service.close()

    service.issue_service.close.assert_awaited_once()

    service.comment_service.close.assert_awaited_once()

    service.timeline_service.close.assert_awaited_once()
