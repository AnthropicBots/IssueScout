from __future__ import annotations

from issuescout.cli.commands import version


def test_version_command(capsys):
    version.run()

    output = capsys.readouterr().out

    assert "IssueScout" in output
    assert "Python" in output
