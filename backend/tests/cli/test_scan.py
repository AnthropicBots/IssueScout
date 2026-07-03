from __future__ import annotations

from issuescout.cli.commands import scan
from issuescout.models.scan_result import (
    IssueSummary,
    ScanResult,
)


class FakeEngine:
    async def scan_repository(
        self,
        owner: str,
        repository: str,
    ):
        return ScanResult(
            repository=f"{owner}/{repository}",
            total_issues=10,
            available_issues=1,
            issues=[
                IssueSummary(
                    number=1,
                    title="Fix login",
                    assigned=False,
                    assignee=None,
                    confidence=95,
                    linked_pr_number=10,
                    linked_pr_title="Fix login bug",
                )
            ],
        )


def test_scan_console(monkeypatch, capsys):
    monkeypatch.setattr(
        scan,
        "ScannerEngine",
        FakeEngine,
    )

    scan.run(
        "owner",
        "repo",
        "console",
    )

    output = capsys.readouterr().out

    assert "IssueScout Scan" in output
    assert "owner/repo" in output
    assert "#1 - Fix login" in output


def test_scan_json(monkeypatch, capsys):
    monkeypatch.setattr(
        scan,
        "ScannerEngine",
        FakeEngine,
    )

    scan.run(
        "owner",
        "repo",
        "json",
    )

    output = capsys.readouterr().out

    assert '"repository"' in output
