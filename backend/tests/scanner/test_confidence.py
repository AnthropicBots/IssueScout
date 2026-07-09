from datetime import (
    datetime,
    timedelta,
    timezone,
)

from issuescout.models import (
    AnalysisResult,
    Issue,
)

from issuescout.scanner.confidence import (
    ConfidenceCalculator,
)


def make_issue(
    *,
    labels: list[str] | None = None,
    milestone: str | None = None,
    updated_days_ago: int | None = None,
) -> Issue:

    updated_at = None

    if updated_days_ago is not None:
        updated_at = datetime.now(timezone.utc) - timedelta(days=updated_days_ago)

    return Issue(
        number=1,
        title="Issue",
        body="Body",
        state="open",
        author="octocat",
        labels=labels or [],
        assignees=[],
        milestone=milestone,
        updated_at=updated_at,
    )


def make_result(
    score: int,
    passed: bool,
) -> AnalysisResult:

    return AnalysisResult(
        analyzer="test",
        passed=passed,
        score=score,
        reason="reason",
    )


def test_empty_results():

    calculator = ConfidenceCalculator()

    assert calculator.calculate([]) == 0


def test_single_passed_result():

    calculator = ConfidenceCalculator()

    results = [
        make_result(
            score=20,
            passed=True,
        ),
    ]

    assert calculator.calculate(results) == 20


def test_failed_results_are_ignored():

    calculator = ConfidenceCalculator()

    results = [
        make_result(
            score=20,
            passed=False,
        ),
        make_result(
            score=15,
            passed=False,
        ),
    ]

    assert calculator.calculate(results) == 0


def test_mixed_results():

    calculator = ConfidenceCalculator()

    results = [
        make_result(
            score=20,
            passed=True,
        ),
        make_result(
            score=15,
            passed=False,
        ),
        make_result(
            score=30,
            passed=True,
        ),
    ]

    assert calculator.calculate(results) == 50


def test_multiple_passed_results():

    calculator = ConfidenceCalculator()

    results = [
        make_result(
            score=10,
            passed=True,
        ),
        make_result(
            score=15,
            passed=True,
        ),
        make_result(
            score=25,
            passed=True,
        ),
    ]

    assert calculator.calculate(results) == 50


def test_assignment_and_linked_pr_increase_score():

    calculator = ConfidenceCalculator()

    issue = make_issue()

    results = [
        AnalysisResult(
            analyzer="assignment",
            passed=True,
            score=0,
            reason="",
        ),
        AnalysisResult(
            analyzer="linked_pr",
            passed=True,
            score=0,
            reason="",
        ),
    ]

    assert (
        calculator.calculate(
            issue,
            results,
        )
        == 40
    )


def test_labels_contribute_to_score():

    calculator = ConfidenceCalculator()

    issue = make_issue(
        labels=[
            "good first issue",
            "help wanted",
            "bug",
        ],
    )

    assert (
        calculator.calculate(
            issue,
            [],
        )
        == 35
    )


def test_milestone_adds_score():

    calculator = ConfidenceCalculator()

    issue = make_issue(
        milestone="v1.0",
    )

    assert (
        calculator.calculate(
            issue,
            [],
        )
        == 5
    )


def test_recent_issue_gets_recent_activity_bonus():

    calculator = ConfidenceCalculator()

    issue = make_issue(
        updated_days_ago=10,
    )

    assert (
        calculator.calculate(
            issue,
            [],
        )
        == 15
    )


def test_old_issue_gets_medium_activity_bonus():

    calculator = ConfidenceCalculator()

    issue = make_issue(
        updated_days_ago=60,
    )

    assert (
        calculator.calculate(
            issue,
            [],
        )
        == 8
    )


def test_stale_issue_gets_no_activity_bonus():

    calculator = ConfidenceCalculator()

    issue = make_issue(
        updated_days_ago=120,
    )

    assert (
        calculator.calculate(
            issue,
            [],
        )
        == 0
    )


def test_maximum_score():

    calculator = ConfidenceCalculator()

    issue = make_issue(
        labels=[
            "good first issue",
            "help wanted",
            "bug",
        ],
        milestone="v1",
        updated_days_ago=1,
    )

    results = [
        AnalysisResult(
            analyzer="assignment",
            passed=True,
            score=0,
            reason="",
        ),
        AnalysisResult(
            analyzer="linked_pr",
            passed=True,
            score=0,
            reason="",
        ),
    ]

    assert (
        calculator.calculate(
            issue,
            results,
        )
        == 95
    )


def test_failed_analysis_results_do_not_increase_score():

    calculator = ConfidenceCalculator()

    issue = make_issue()

    results = [
        AnalysisResult(
            analyzer="assignment",
            passed=False,
            score=0,
            reason="",
        ),
        AnalysisResult(
            analyzer="linked_pr",
            passed=False,
            score=0,
            reason="",
        ),
    ]

    assert (
        calculator.calculate(
            issue,
            results,
        )
        == 0
    )
