from issuescout.scanner.intelligence.pull_request import (
    PullRequestDiscussionAnalyzer,
)


def test_detects_resolution_keywords():

    analyzer = PullRequestDiscussionAnalyzer()

    result = analyzer.analyze(
        "This PR fixes the issue and has been approved.",
    )

    assert result["matched"] is True
    assert "fixes" in result["keywords"]
    assert result["confidence"] > 0


def test_returns_no_match_for_unrelated_text():

    analyzer = PullRequestDiscussionAnalyzer()

    result = analyzer.analyze(
        "Minor formatting update.",
    )

    assert result["matched"] is False
    assert result["keywords"] == []
    assert result["confidence"] == 0


def test_detects_approval():

    analyzer = PullRequestDiscussionAnalyzer()

    result = analyzer.analyze(
        "Approved. Merged. Fixes issue.",
    )

    assert result["approval_count"] == 1
    assert result["merged"] is True


def test_negative_review_reduces_confidence():

    analyzer = PullRequestDiscussionAnalyzer()

    result = analyzer.analyze(
        ("Changes requested. This does not fix the issue."),
    )

    assert result["confidence"] == 0

    assert "does not fix" in result["negative_keywords"]
