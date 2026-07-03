from types import SimpleNamespace

from issuescout.output.console import ConsoleFormatter


def test_console_prints_explanation(capsys):
    prediction = SimpleNamespace(
        prediction=SimpleNamespace(
            pull_request=SimpleNamespace(number=123),
            score=95,
        ),
        candidates=[],
        confidence="High",
        threshold=80,
        accepted=True,
        issue_number=10,
        explanation=SimpleNamespace(
            items=[
                SimpleNamespace(
                    analyzer="title_similarity",
                    score=25,
                    reason="Titles are similar",
                )
            ],
            summary="Prediction explanation summary.",
        ),
    )

    ConsoleFormatter().display(prediction)

    output = capsys.readouterr().out

    assert "Evidence" in output
    assert "Titles are similar" in output
    assert "Prediction explanation summary." in output
