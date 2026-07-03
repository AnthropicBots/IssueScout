from issuescout.output.console import ConsoleFormatter


def test_console_formatter_can_be_created():
    formatter = ConsoleFormatter()

    assert formatter is not None


def test_console_formatter_has_display():
    formatter = ConsoleFormatter()

    assert hasattr(formatter, "display")
