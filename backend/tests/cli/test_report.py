from __future__ import annotations

from issuescout.cli.commands.report import report
from issuescout.evaluation.report import (
    EvaluationReport,
    RepositoryMetrics,
)


def test_report_factory():
    result = report(
        "owner/repository",
    )

    assert isinstance(
        result,
        EvaluationReport,
    )

    assert result.repository == "owner/repository"

    assert isinstance(
        result.metrics,
        RepositoryMetrics,
    )

    assert result.failures == []

    assert result.metadata == {}
