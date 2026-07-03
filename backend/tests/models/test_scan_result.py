from issuescout.models.scan_result import (
    IssueSummary,
    ScanResult,
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
