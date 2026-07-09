import pytest

from issuescout.application.resolution import (
    ResolutionAnalyzer,
)
from issuescout.domain.models import (
    CandidatePullRequestDetails,
)


def test_analyzer_scores_matching_pr():

    analyzer = ResolutionAnalyzer()

    result = analyzer.analyze(
        issue_title="Fix login bug",
        issue_body="Login crashes after submit button click.",
        candidate=CandidatePullRequestDetails(
            number=1,
            title="Fix login bug",
            body="Login crashes after submit button click.",
            state="open",
            merged=True,
            author="alice",
            review_count=2,
            comment_count=3,
        ),
    )

    assert result.confidence > 50

    assert "merged" in result.passed_checks
    assert len(result.evidence.items) >= 3

    assert any(item.type == "merged" for item in result.evidence.items)

    assert result.evidence.total_weight > 0

    assert result.evidence.passed_weight > 0


def test_analyzer_returns_low_score_for_unrelated_pr():

    analyzer = ResolutionAnalyzer()

    result = analyzer.analyze(
        issue_title="Fix login bug",
        issue_body="Login crashes",
        candidate=CandidatePullRequestDetails(
            number=2,
            title="Add dark mode",
            body="Adds dark mode support.",
            state="open",
            merged=False,
            author="alice",
        ),
    )

    assert result.confidence < 40
    assert result.evidence.items == []

    assert result.evidence.total_weight == 0

    assert result.evidence.passed_weight == 0


def test_discussion_intelligence_increases_score():

    analyzer = ResolutionAnalyzer()

    candidate = CandidatePullRequestDetails(
        number=1,
        title="Fix login bug",
        body="Fix login",
        state="closed",
        merged=True,
        author="alice",
        discussion_confidence=100,
    )

    result = analyzer.analyze(
        "Fix login bug",
        "Fix login",
        candidate,
    )

    assert "review_discussion" in result.passed_checks

    assert result.evidence.total_weight > 0

    assert any(item.type == "merged" for item in result.evidence.items)


def test_evidence_summary_contains_expected_items():

    analyzer = ResolutionAnalyzer()

    result = analyzer.analyze(
        issue_title="Fix login bug",
        issue_body="Login crashes after clicking submit.",
        candidate=CandidatePullRequestDetails(
            number=10,
            title="Fix login bug",
            body="Login crashes after clicking submit.",
            state="closed",
            merged=True,
            author="alice",
            review_count=2,
            comment_count=1,
        ),
    )

    evidence_types = {item.type for item in result.evidence.items}

    assert "title_similarity" in evidence_types
    assert "merged" in evidence_types
    assert "reviews" in evidence_types
    assert "discussion" in evidence_types

    assert result.evidence.passed_weight > 0
    assert result.evidence.total_weight >= (result.evidence.passed_weight)


@pytest.mark.anyio
async def test_title_not_matching():

    analyzer = ResolutionAnalyzer()

    candidate = CandidatePullRequestDetails(
        number=1,
        title="Refactor networking",
        body="",
        state="open",
        author="alice",
        merged=False,
        review_count=0,
        changed_files=[],
        commits=[],
        comment_count=0,
        discussion_confidence=0,
    )

    result = analyzer.analyze(
        "Fix login",
        None,
        candidate,
    )

    assert "title" not in result.passed_checks
    assert result.confidence == 0
    assert result.verdict == "Unlikely"


@pytest.mark.anyio
async def test_body_similarity_below_threshold():

    analyzer = ResolutionAnalyzer()

    candidate = CandidatePullRequestDetails(
        number=1,
        title="Refactor networking",
        body="",
        state="open",
        author="alice",
        merged=False,
        review_count=0,
        changed_files=[],
        commits=[],
        comment_count=0,
        discussion_confidence=0,
    )

    result = analyzer.analyze(
        "Fix login",
        "one two three four five six",
        candidate,
    )

    assert "body" not in result.passed_checks


@pytest.mark.anyio
async def test_body_similarity_above_threshold():

    analyzer = ResolutionAnalyzer()

    candidate = CandidatePullRequestDetails(
        number=1,
        title="Anything",
        body="one two three four five six seven",
        state="open",
        author="alice",
        merged=False,
        review_count=0,
        changed_files=[],
        commits=[],
        comment_count=0,
        discussion_confidence=0,
    )

    result = analyzer.analyze(
        "Fix login",
        "one two three four five six",
        candidate,
    )

    assert "body" in result.passed_checks


@pytest.mark.anyio
async def test_merged_pull_request():

    analyzer = ResolutionAnalyzer()

    candidate = CandidatePullRequestDetails(
        number=1,
        title="",
        body="",
        state="closed",
        author="alice",
        merged=True,
        review_count=0,
        changed_files=[],
        commits=[],
        comment_count=0,
        discussion_confidence=0,
    )

    result = analyzer.analyze(
        "",
        None,
        candidate,
    )

    assert "merged" in result.passed_checks


@pytest.mark.anyio
async def test_review_evidence():

    analyzer = ResolutionAnalyzer()

    candidate = CandidatePullRequestDetails(
        number=1,
        title="",
        body="",
        state="open",
        author="alice",
        merged=False,
        review_count=3,
        changed_files=[],
        commits=[],
        comment_count=0,
        discussion_confidence=0,
    )

    result = analyzer.analyze(
        "",
        None,
        candidate,
    )

    assert "reviews" in result.passed_checks


@pytest.mark.anyio
async def test_changed_files():

    analyzer = ResolutionAnalyzer()

    candidate = CandidatePullRequestDetails(
        number=1,
        title="",
        body="",
        state="open",
        author="alice",
        merged=False,
        review_count=0,
        changed_files=["a.py"],
        commits=[],
        comment_count=0,
        discussion_confidence=0,
    )

    result = analyzer.analyze(
        "",
        None,
        candidate,
    )

    assert "files" in result.passed_checks


@pytest.mark.anyio
async def test_commit_evidence():

    analyzer = ResolutionAnalyzer()

    candidate = CandidatePullRequestDetails(
        number=1,
        title="",
        body="",
        state="open",
        author="alice",
        merged=False,
        review_count=0,
        changed_files=[],
        commits=["commit"],
        comment_count=0,
        discussion_confidence=0,
    )

    result = analyzer.analyze(
        "",
        None,
        candidate,
    )

    assert "commits" in result.passed_checks


@pytest.mark.anyio
async def test_discussion_evidence():

    analyzer = ResolutionAnalyzer()

    candidate = CandidatePullRequestDetails(
        number=1,
        title="",
        body="",
        state="open",
        author="alice",
        merged=False,
        review_count=0,
        changed_files=[],
        commits=[],
        comment_count=5,
        discussion_confidence=0,
    )

    result = analyzer.analyze(
        "",
        None,
        candidate,
    )

    assert "discussion" in result.passed_checks


@pytest.mark.anyio
async def test_discussion_intelligence():

    analyzer = ResolutionAnalyzer()

    candidate = CandidatePullRequestDetails(
        number=1,
        title="",
        body="",
        state="open",
        author="alice",
        merged=False,
        review_count=0,
        changed_files=[],
        commits=[],
        comment_count=0,
        discussion_confidence=70,
    )

    result = analyzer.analyze(
        "",
        None,
        candidate,
    )

    assert "discussion_intelligence" in result.passed_checks
