from unittest.mock import Mock

import issuescout.__main__ as entry


def test_main_invokes_main(monkeypatch):
    called = Mock()

    monkeypatch.setattr(
        entry,
        "main",
        called,
    )

    entry.main()

    called.assert_called_once()
