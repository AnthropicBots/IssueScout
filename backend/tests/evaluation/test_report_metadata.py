from issuescout.evaluation.report import EvaluationReport


def test_report_metadata():
    report = EvaluationReport(
        repository="owner/repo",
    )

    report.metadata["branch"] = "main"

    assert report.metadata["branch"] == "main"
    assert report.failures == []
    assert report.repository == "owner/repo"
