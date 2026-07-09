from issuescout.models.scan_result import (
    IssueSummary,
    ScanResult,
)
from issuescout.models.scan_result import (
    CandidatePullRequestSummary,
)
from issuescout.evidence.model import (
    EvidenceItem,
)


def test_issue_summary():
    issue = IssueSummary(
        number=1,
        title="Bug",
        assigned=False,
        assignee=None,
        confidence=80,
    )

    assert issue.number == 1
    assert issue.linked_pr_number is None


def test_scan_result():
    result = ScanResult(
        repository="owner/repo",
        total_issues=10,
        available_issues=2,
        issues=[],
    )

    assert result.repository == "owner/repo"
    assert result.issues == []


def test_candidate_summary():

    summary = CandidatePullRequestSummary(
        number=1,
        title="Fix login",
        confidence=92,
        url="https://github.com/example/repo/pull/1",
        sources=["comment"],
        reasons=["Maintainer linked PR"],
        evidence=[
            EvidenceItem(
                type="merged",
                label="Merged",
                description="PR merged.",
                weight=20,
                passed=True,
            ),
        ],
    )

    assert summary.number == 1
    assert summary.confidence == 92


def test_issue_summary_supports_candidate_pull_requests():

    summary = IssueSummary(
        number=1,
        title="Issue",
        assigned=False,
        assignee=None,
        confidence=90,
        candidate_count=1,
        candidate_pull_requests=[
            CandidatePullRequestSummary(
                number=123,
                title="Fix issue",
                confidence=95,
                url="https://github.com/example/repo/pull/123",
                sources=["comment", "timeline"],
                reasons=["Maintainer linked PR"],
                evidence=[
                    EvidenceItem(
                        type="timeline",
                        label="Timeline Reference",
                        description="Timeline references the issue.",
                        weight=20,
                        passed=True,
                    ),
                ],
            )
        ],
    )

    assert summary.candidate_count == 1
    assert summary.candidate_pull_requests[0].number == 123


def test_candidate_summary_contains_evidence():

    summary = CandidatePullRequestSummary(
        number=7,
        title="Fix crash",
        confidence=97,
        url="https://github.com/example/repo/pull/7",
        sources=["timeline"],
        reasons=["Merged"],
        evidence=[
            EvidenceItem(
                type="merged",
                label="Merged",
                description="Pull request merged.",
                weight=20,
                passed=True,
            ),
            EvidenceItem(
                type="reviews",
                label="Reviews",
                description="Maintainer approved.",
                weight=10,
                passed=True,
            ),
        ],
    )

    assert len(summary.evidence) == 2
    assert summary.evidence[0].type == "merged"
    assert summary.evidence[1].passed is True
    assert summary.evidence[0].weight == 20
