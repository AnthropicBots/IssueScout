from unittest.mock import AsyncMock

import pytest

from issuescout.application.candidate.candidate_enricher import (
    CandidatePullRequestEnricher,
)
from issuescout.domain.models import (
    CandidatePullRequest,
)


@pytest.mark.anyio
async def test_enrich_candidate():

    enricher = CandidatePullRequestEnricher()

    enricher.pull_request_service.get_pull_request = AsyncMock(
        return_value={
            "number": 69607,
            "title": "Fix docs",
            "body": "Body",
            "state": "open",
            "merged": False,
            "user": {
                "login": "alice",
            },
            "labels": [],
        }
    )

    enricher.pull_request_service.get_pull_request_files = AsyncMock(
        return_value=[
            {
                "filename": "src/app.ts",
            }
        ]
    )

    enricher.pull_request_service.get_pull_request_commits = AsyncMock(
        return_value=[
            {
                "commit": {
                    "message": "Fix login bug",
                }
            }
        ]
    )

    enricher.pull_request_service.get_pull_request_reviews = AsyncMock(
        return_value=[],
    )

    enricher.pull_request_service.get_pull_request_comments = AsyncMock(
        return_value=[
            {
                "body": "Approved. Fixes issue.",
            }
        ],
    )

    result = await enricher.enrich(
        "angular",
        "angular",
        CandidatePullRequest(
            number=69607,
            url="url",
            sources={"comment"},
        ),
    )

    assert result.number == 69607
    assert result.title == "Fix docs"
    assert result.author == "alice"
    assert result.discussion_confidence > 0
    assert "approved" in result.discussion_keywords

    assert result.changed_files == {
        "src/app.ts",
    }

    assert result.commits == [
        "Fix login bug",
    ]
