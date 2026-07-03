from __future__ import annotations

import sys
from unittest.mock import Mock

from issuescout.cli import main


def test_build_parser_contains_expected_commands():
    parser = main.build_parser()

    subparser_action = next(
        action for action in parser._actions if getattr(action, "choices", None)
    )

    assert set(subparser_action.choices) == {
        "evaluate",
        "scan",
        "dataset",
        "version",
    }


def test_main_runs_evaluate(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "issuescout",
            "evaluate",
            "dataset.json",
        ],
    )

    called = Mock()

    monkeypatch.setattr(
        main,
        "run_evaluate",
        called,
    )

    main.main()

    called.assert_called_once_with(
        "dataset.json",
    )


def test_main_runs_scan(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "issuescout",
            "scan",
            "owner",
            "repo",
            "--format",
            "json",
        ],
    )

    called = Mock()

    monkeypatch.setattr(
        main,
        "run_scan",
        called,
    )

    main.main()

    called.assert_called_once_with(
        "owner",
        "repo",
        "json",
    )


def test_main_runs_dataset(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "issuescout",
            "dataset",
            "owner",
            "repo",
            "--limit",
            "25",
        ],
    )

    called = Mock()

    monkeypatch.setattr(
        main,
        "run_dataset",
        called,
    )

    main.main()

    called.assert_called_once_with(
        "owner",
        "repo",
        25,
    )


def test_main_runs_version(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "issuescout",
            "version",
        ],
    )

    called = Mock()

    monkeypatch.setattr(
        main,
        "run_version",
        called,
    )

    main.main()

    called.assert_called_once()


def test_main_without_command_prints_help(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "issuescout",
        ],
    )

    help_mock = Mock()

    parser = main.build_parser()

    monkeypatch.setattr(
        parser,
        "print_help",
        help_mock,
    )

    monkeypatch.setattr(
        main,
        "build_parser",
        lambda: parser,
    )

    main.main()

    help_mock.assert_called_once()
