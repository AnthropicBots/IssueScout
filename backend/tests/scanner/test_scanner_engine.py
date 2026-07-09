from unittest.mock import AsyncMock, Mock

import pytest

from issuescout.models import (
    AnalysisResult,
    Repository,
    RepositoryScanContext,
)
from issuescout.scanner.engine import ScannerEngine

from tests.helpers.factories import (
    make_issue,
    make_pull_request,
)
from issuescout.domain.models import (
    CandidatePullRequestDetails,
)


@pytest.fixture
def repository():
    return Repository(
        owner="python",
        name="cpython",
    )


@pytest.fixture
def passing_result():
    return AnalysisResult(
        analyzer="assignment",
        passed=True,
        score=100,
        reason="passed",
    )


@pytest.fixture
def failing_result():
    return AnalysisResult(
        analyzer="assignment",
        passed=False,
        score=0,
        reason="failed",
    )


def mock_candidate_enricher(engine: ScannerEngine) -> None:
    engine.candidate_enricher = AsyncMock()

    engine.candidate_enricher.enrich.return_value = CandidatePullRequestDetails(
        number=1,
        title="Mock PR",
        body="",
        state="closed",
        merged=True,
        author="alice",
    )


@pytest.mark.anyio
async def test_scan_repository_returns_scan_result(
    repository,
    passing_result,
):
    issue = make_issue(
        number=123,
        title="Fix login bug",
        assigned=True,
        assignee="alice",
    )

    pr = make_pull_request(
        number=42,
        title="Fix login bug",
    )

    context = RepositoryScanContext(
        repository=repository,
        issues=[issue],
        pull_requests=[pr],
    )

    fetcher = AsyncMock()
    fetcher.fetch_context.return_value = context

    detector = AsyncMock()
    detector.find_linked_pr.return_value = pr

    pipeline = AsyncMock()
    pipeline.run.return_value = [
        passing_result,
    ]

    confidence = Mock()
    confidence.calculate.return_value = 95

    engine = ScannerEngine(
        fetcher=fetcher,
        detector=detector,
        pipeline=pipeline,
        confidence=confidence,
    )
    mock_candidate_enricher(engine)

    engine.candidate_enricher = AsyncMock()

    engine.candidate_enricher.enrich.return_value = CandidatePullRequestDetails(
        number=42,
        title="Fix login bug",
        body="Fix login bug",
        state="closed",
        merged=True,
        author="alice",
    )

    result = await engine.scan_repository(
        "python",
        "cpython",
    )

    assert result.repository == "python/cpython"
    assert result.total_issues == 1
    assert result.available_issues == 1

    summary = result.issues[0]

    assert summary.number == 123
    assert summary.title == "Fix login bug"
    assert summary.assigned is True
    assert summary.assignee == "alice"
    assert summary.confidence == 95
    assert summary.linked_pr_number == 42
    assert summary.linked_pr_title == "Fix login bug"


@pytest.mark.anyio
async def test_scan_repository_filters_failed_issue(
    repository,
    failing_result,
):
    issue = make_issue()

    context = RepositoryScanContext(
        repository=repository,
        issues=[issue],
    )

    fetcher = AsyncMock()
    fetcher.fetch_context.return_value = context

    detector = AsyncMock()
    detector.find_linked_pr.return_value = None

    pipeline = AsyncMock()
    pipeline.run.return_value = [
        failing_result,
    ]

    confidence = Mock()

    engine = ScannerEngine(
        fetcher=fetcher,
        detector=detector,
        pipeline=pipeline,
        confidence=confidence,
    )
    mock_candidate_enricher(engine)

    result = await engine.scan_repository(
        "python",
        "cpython",
    )

    assert result.total_issues == 0
    assert result.available_issues == 0
    assert result.issues == []

    confidence.calculate.assert_not_called()


@pytest.mark.anyio
async def test_detector_called_for_each_issue(
    repository,
    passing_result,
):
    issues = [
        make_issue(number=1),
        make_issue(number=2),
        make_issue(number=3),
    ]

    context = RepositoryScanContext(
        repository=repository,
        issues=issues,
    )

    fetcher = AsyncMock()
    fetcher.fetch_context.return_value = context

    detector = AsyncMock()
    detector.find_linked_pr.return_value = None

    pipeline = AsyncMock()
    pipeline.run.return_value = [passing_result]

    confidence = Mock()
    confidence.calculate.return_value = 100

    engine = ScannerEngine(
        fetcher=fetcher,
        detector=detector,
        pipeline=pipeline,
        confidence=confidence,
    )
    mock_candidate_enricher(engine)

    await engine.scan_repository(
        "python",
        "cpython",
    )

    assert detector.find_linked_pr.await_count == 3


@pytest.mark.anyio
async def test_pipeline_called_for_each_issue(
    repository,
    passing_result,
):
    issues = [
        make_issue(number=1),
        make_issue(number=2),
    ]

    context = RepositoryScanContext(
        repository=repository,
        issues=issues,
    )

    fetcher = AsyncMock()
    fetcher.fetch_context.return_value = context

    detector = AsyncMock()
    detector.find_linked_pr.return_value = None

    pipeline = AsyncMock()
    pipeline.run.return_value = [passing_result]

    confidence = Mock()
    confidence.calculate.return_value = 100

    engine = ScannerEngine(
        fetcher=fetcher,
        detector=detector,
        pipeline=pipeline,
        confidence=confidence,
    )
    mock_candidate_enricher(engine)

    await engine.scan_repository(
        "python",
        "cpython",
    )

    assert pipeline.run.await_count == 2


@pytest.mark.anyio
async def test_confidence_calculated_for_each_accepted_issue(
    repository,
    passing_result,
):
    issues = [
        make_issue(number=1),
        make_issue(number=2),
    ]

    context = RepositoryScanContext(
        repository=repository,
        issues=issues,
    )

    fetcher = AsyncMock()
    fetcher.fetch_context.return_value = context

    detector = AsyncMock()
    detector.find_linked_pr.return_value = None

    pipeline = AsyncMock()
    pipeline.run.return_value = [passing_result]

    confidence = Mock()
    confidence.calculate.return_value = 87

    engine = ScannerEngine(
        fetcher=fetcher,
        detector=detector,
        pipeline=pipeline,
        confidence=confidence,
    )
    mock_candidate_enricher(engine)

    await engine.scan_repository(
        "python",
        "cpython",
    )

    assert confidence.calculate.call_count == 2


@pytest.mark.anyio
async def test_scan_repository_handles_missing_linked_pr(
    repository,
    passing_result,
):
    issue = make_issue()

    context = RepositoryScanContext(
        repository=repository,
        issues=[issue],
    )

    fetcher = AsyncMock()
    fetcher.fetch_context.return_value = context

    detector = AsyncMock()
    detector.find_linked_pr.return_value = None

    pipeline = AsyncMock()
    pipeline.run.return_value = [passing_result]

    confidence = Mock()
    confidence.calculate.return_value = 75

    engine = ScannerEngine(
        fetcher=fetcher,
        detector=detector,
        pipeline=pipeline,
        confidence=confidence,
    )
    mock_candidate_enricher(engine)

    result = await engine.scan_repository(
        "python",
        "cpython",
    )

    summary = result.issues[0]

    assert summary.linked_pr_number is None
    assert summary.linked_pr_title is None


@pytest.mark.anyio
async def test_fetcher_closed_after_scan(
    repository,
    passing_result,
):
    issue = make_issue()

    context = RepositoryScanContext(
        repository=repository,
        issues=[issue],
    )

    fetcher = AsyncMock()
    fetcher.fetch_context.return_value = context

    detector = AsyncMock()
    detector.find_linked_pr.return_value = None

    pipeline = AsyncMock()
    pipeline.run.return_value = [passing_result]

    confidence = Mock()
    confidence.calculate.return_value = 100

    engine = ScannerEngine(
        fetcher=fetcher,
        detector=detector,
        pipeline=pipeline,
        confidence=confidence,
    )
    mock_candidate_enricher(engine)

    await engine.scan_repository(
        "python",
        "cpython",
    )

    fetcher.close.assert_awaited_once()


@pytest.mark.anyio
async def test_detector_closed_after_scan(
    repository,
    passing_result,
):
    issue = make_issue()

    context = RepositoryScanContext(
        repository=repository,
        issues=[issue],
    )

    fetcher = AsyncMock()
    fetcher.fetch_context.return_value = context

    detector = AsyncMock()
    detector.find_linked_pr.return_value = None

    pipeline = AsyncMock()
    pipeline.run.return_value = [passing_result]

    confidence = Mock()
    confidence.calculate.return_value = 100

    engine = ScannerEngine(
        fetcher=fetcher,
        detector=detector,
        pipeline=pipeline,
        confidence=confidence,
    )
    mock_candidate_enricher(engine)

    await engine.scan_repository(
        "python",
        "cpython",
    )

    detector.close.assert_awaited_once()


@pytest.mark.anyio
async def test_progress_callback_called_for_empty_repository(
    repository,
):
    context = RepositoryScanContext(
        repository=repository,
        issues=[],
    )

    fetcher = AsyncMock()
    fetcher.fetch_context.return_value = context

    detector = AsyncMock()

    callback = Mock()

    engine = ScannerEngine(
        fetcher=fetcher,
        detector=detector,
    )
    mock_candidate_enricher(engine)

    await engine.scan_repository(
        "python",
        "cpython",
        progress_callback=callback,
    )

    callback.assert_called_once_with(
        0,
        0,
    )


@pytest.mark.anyio
async def test_detect_linked_pr_returns_none_on_exception(
    repository,
):
    issue = make_issue(
        number=123,
    )

    context = RepositoryScanContext(
        repository=repository,
        issues=[issue],
    )

    fetcher = AsyncMock()

    detector = AsyncMock()
    detector.find_linked_pr.side_effect = RuntimeError(
        "GitHub unavailable",
    )

    engine = ScannerEngine(
        fetcher=fetcher,
        detector=detector,
    )
    mock_candidate_enricher(engine)

    issue_number, linked_pr = await engine._detect_linked_pr(
        context,
        issue,
    )

    assert issue_number == 123
    assert linked_pr is None


@pytest.mark.anyio
async def test_detect_linked_pr_returns_pull_request(
    repository,
):
    issue = make_issue(
        number=55,
    )

    pr = make_pull_request(
        number=999,
    )

    context = RepositoryScanContext(
        repository=repository,
        issues=[issue],
    )

    fetcher = AsyncMock()

    detector = AsyncMock()
    detector.find_linked_pr.return_value = pr

    engine = ScannerEngine(
        fetcher=fetcher,
        detector=detector,
    )
    mock_candidate_enricher(engine)

    issue_number, linked_pr = await engine._detect_linked_pr(
        context,
        issue,
    )

    assert issue_number == 55
    assert linked_pr is pr


@pytest.mark.anyio
async def test_fetch_missing_pull_requests_ignores_fetch_errors():
    engine = ScannerEngine()
    mock_candidate_enricher(engine)

    engine.fetcher = AsyncMock()

    engine.fetcher.fetch_pull_request.side_effect = RuntimeError()

    context = Mock()
    context.pull_request_lookup = {}

    resolved = []

    await engine._fetch_missing_pull_requests(
        owner="python",
        repo="cpython",
        context=context,
        resolved_pull_requests=resolved,
        missing_pull_requests={123},
    )

    assert resolved == []

    assert context.pull_request_lookup == {}


@pytest.mark.anyio
async def test_fetch_missing_pull_requests_skips_cached_pull_requests():
    engine = ScannerEngine()
    mock_candidate_enricher(engine)

    engine.fetcher = AsyncMock()

    context = Mock()

    context.pull_request_lookup = {
        123: Mock(),
    }

    resolved = []

    await engine._fetch_missing_pull_requests(
        owner="python",
        repo="cpython",
        context=context,
        resolved_pull_requests=resolved,
        missing_pull_requests={123},
    )

    engine.fetcher.fetch_pull_request.assert_not_awaited()

    assert resolved == []
