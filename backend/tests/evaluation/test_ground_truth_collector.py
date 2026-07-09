from unittest.mock import AsyncMock
from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

from issuescout.evaluation.ground_truth import (
    GroundTruthCollector,
)

pytestmark = pytest.mark.anyio


async def test_ground_truth_collector_is_abstract():

    collector = GroundTruthCollector()

    assert collector is not None


async def test_collect_builds_ground_truth_record():

    with (
        patch(
            "issuescout.evaluation.ground_truth.IssueService",
        ) as MockIssueService,
        patch(
            "issuescout.evaluation.ground_truth.TimelineService",
        ) as MockTimelineService,
        patch(
            "issuescout.evaluation.ground_truth.TimelineRelationResolver",
        ) as MockResolver,
    ):
        issue_service = MockIssueService.return_value
        timeline_service = MockTimelineService.return_value
        resolver = MockResolver.return_value

        issue_service.get_issue = AsyncMock(
            return_value={
                "title": "Fix login bug",
                "state": "closed",
                "created_at": "2024-01-01T10:00:00Z",
                "closed_at": "2024-01-03T12:00:00Z",
            },
        )

        timeline_service.get_issue_timeline = AsyncMock(
            return_value=[
                {
                    "event": "cross-referenced",
                },
            ],
        )

        resolver.resolve.return_value = MagicMock(
            pull_request_number=123,
            linkage_method="timeline",
        )

        collector = GroundTruthCollector()

        result = await collector.collect(
            "python",
            "cpython",
            101,
        )

        assert result.repository_owner == "python"
        assert result.repository_name == "cpython"
        assert result.issue_number == 101
        assert result.issue_title == "Fix login bug"
        assert result.issue_state == "closed"
        assert result.actual_pull_request == 123
        assert result.linkage_method == "timeline"

        assert result.issue_created_at is not None
        assert result.issue_closed_at is not None


async def test_collect_uses_default_values():

    with (
        patch(
            "issuescout.evaluation.ground_truth.IssueService",
        ) as MockIssueService,
        patch(
            "issuescout.evaluation.ground_truth.TimelineService",
        ) as MockTimelineService,
        patch(
            "issuescout.evaluation.ground_truth.TimelineRelationResolver",
        ) as MockResolver,
    ):
        issue_service = MockIssueService.return_value
        timeline_service = MockTimelineService.return_value
        resolver = MockResolver.return_value

        issue_service.get_issue = AsyncMock(
            return_value={},
        )

        timeline_service.get_issue_timeline = AsyncMock(
            return_value=[],
        )

        resolver.resolve.return_value = MagicMock(
            pull_request_number=None,
            linkage_method="none",
        )

        collector = GroundTruthCollector()

        result = await collector.collect(
            "owner",
            "repo",
            1,
        )

        assert result.issue_title == ""
        assert result.issue_state == "unknown"
        assert result.actual_pull_request is None
        assert result.issue_created_at is None
        assert result.issue_closed_at is None


async def test_close_closes_services():

    with (
        patch(
            "issuescout.evaluation.ground_truth.IssueService",
        ) as MockIssueService,
        patch(
            "issuescout.evaluation.ground_truth.TimelineService",
        ) as MockTimelineService,
    ):
        issue_service = MockIssueService.return_value
        timeline_service = MockTimelineService.return_value

        issue_service.close = AsyncMock()
        timeline_service.close = AsyncMock()

        collector = GroundTruthCollector()

        await collector.close()

        issue_service.close.assert_awaited_once()
        timeline_service.close.assert_awaited_once()
