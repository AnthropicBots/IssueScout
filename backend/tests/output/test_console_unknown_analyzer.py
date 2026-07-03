from types import SimpleNamespace

from issuescout.output.console import ConsoleFormatter


def test_console_handles_unknown_analyzer(capsys):
    prediction = SimpleNamespace(
        prediction=SimpleNamespace(
            pull_request=SimpleNamespace(number=55),
            score=80,
        ),
        candidates=[],
        confidence="Medium",
        threshold=60,
        accepted=True,
        issue_number=7,
        explanation=SimpleNamespace(
            items=[
                SimpleNamespace(
                    analyzer="unknown_custom_rule",
                    score=10,
                    reason="Custom reason",
                )
            ],
            summary="Done",
        ),
    )

    ConsoleFormatter().display(prediction)

    output = capsys.readouterr().out

    assert "Unknown Custom Rule" in output
    assert "Other" in output
    assert "Custom reason" in output
