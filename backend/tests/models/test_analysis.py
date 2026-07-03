from issuescout.models.analysis import AnalysisResult


def test_analysis_result():
    result = AnalysisResult(
        analyzer="title",
        passed=True,
        score=15,
        reason="Matched title",
    )

    assert result.analyzer == "title"
    assert result.passed is True
    assert result.score == 15
    assert result.reason == "Matched title"
