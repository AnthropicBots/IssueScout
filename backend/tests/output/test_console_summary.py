from types import SimpleNamespace

from issuescout.output.console import ConsoleFormatter


def test_console_prints_summary_section(capsys):
    prediction = SimpleNamespace(
        prediction=SimpleNamespace(
            pull_request=SimpleNamespace(number=5),
            score=100,
        ),
        candidates=[],
        confidence="Very High",
        threshold=70,
        accepted=True,
        issue_number=1,
        explanation=SimpleNamespace(
            items=[],
            summary="Overall prediction summary.",
        ),
    )

    ConsoleFormatter().display(prediction)

    output = capsys.readouterr().out

    assert "Summary" in output
    assert "Overall prediction summary." in output
