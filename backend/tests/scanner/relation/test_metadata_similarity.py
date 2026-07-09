import pytest
from datetime import datetime, timedelta

from issuescout.scanner.relation.metadata_similarity import (
    MetadataSimilarityAnalyzer,
)

from tests.helpers.factories import (
    make_issue,
    make_pull_request,
)


@pytest.mark.anyio
async def test_same_author_and_recent_pr():

    analyzer = MetadataSimilarityAnalyzer()

    created = datetime.now()

    issue = make_issue(
        author="alice",
        created_at=created,
    )

    pr = make_pull_request(
        author="alice",
        created_at=created + timedelta(days=2),
    )

    result = await analyzer.analyze(
        issue,
        pr,
    )

    assert result.score > 0
    assert result.confidence > 0


@pytest.mark.anyio
async def test_same_author_only():

    analyzer = MetadataSimilarityAnalyzer()

    issue = make_issue(
        author="alice",
    )

    pr = make_pull_request(
        author="alice",
    )

    result = await analyzer.analyze(
        issue,
        pr,
    )

    assert result.score == 5
    assert result.confidence == 30


@pytest.mark.anyio
async def test_no_metadata_match():

    analyzer = MetadataSimilarityAnalyzer()

    created = datetime.now()

    issue = make_issue(
        author="alice",
        created_at=created,
    )

    pr = make_pull_request(
        author="bob",
        created_at=created - timedelta(days=1),
    )

    result = await analyzer.analyze(
        issue,
        pr,
    )

    assert result.score == 0
    assert result.confidence == 0


@pytest.mark.anyio
async def test_pr_created_within_thirty_days():

    analyzer = MetadataSimilarityAnalyzer()

    created = datetime.now()

    issue = make_issue(
        author="alice",
        created_at=created,
    )

    pr = make_pull_request(
        author="bob",
        created_at=created + timedelta(days=20),
    )

    result = await analyzer.analyze(
        issue,
        pr,
    )

    assert result.score == 3
    assert result.confidence == 50
    assert result.details["created_after_days"] == 20


@pytest.mark.anyio
async def test_recent_issue_update_before_pr():

    analyzer = MetadataSimilarityAnalyzer()

    created = datetime.now()

    issue = make_issue(
        author="alice",
        created_at=created,
        updated_at=created + timedelta(days=38),
    )

    pr = make_pull_request(
        author="bob",
        created_at=created + timedelta(days=40),
    )

    result = await analyzer.analyze(
        issue,
        pr,
    )

    assert result.score == 2
    assert result.confidence == 20
    assert result.details["updated_after_days"] == 2


@pytest.mark.anyio
async def test_score_and_confidence_are_capped():

    analyzer = MetadataSimilarityAnalyzer()

    created = datetime.now()

    issue = make_issue(
        author="alice",
        created_at=created,
        updated_at=created + timedelta(days=1),
    )

    pr = make_pull_request(
        author="alice",
        created_at=created + timedelta(days=2),
    )

    result = await analyzer.analyze(
        issue,
        pr,
    )

    assert result.score == analyzer.metadata.weight
    assert result.confidence == 100


@pytest.mark.anyio
async def test_details_when_no_match():

    analyzer = MetadataSimilarityAnalyzer()

    created = datetime.now()

    issue = make_issue(
        author="alice",
        created_at=created,
    )

    pr = make_pull_request(
        author="bob",
        created_at=created - timedelta(days=10),
    )

    result = await analyzer.analyze(
        issue,
        pr,
    )

    assert result.reason
    assert result.details["same_author"] is False
    assert result.details["created_after_days"] is None
    assert result.details["updated_after_days"] is None
