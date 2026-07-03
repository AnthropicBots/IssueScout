from types import SimpleNamespace

from issuescout.output.console import ConsoleFormatter


def test_console_prints_rejected_prediction(capsys):
    prediction = SimpleNamespace(
        prediction=SimpleNamespace(
            pull_request=SimpleNamespace(number=22),
            score=40,
        ),
        candidates=[],
        confidence="Low",
        threshold=60,
        accepted=False,
        issue_number=3,
        explanation=None,
    )

    ConsoleFormatter().display(prediction)

    output = capsys.readouterr().out

    assert "Prediction rejected" in output
    assert "score below" in output
