from __future__ import annotations

import argparse

from issuescout.cli.commands.evaluate import (
    run as run_evaluate,
)

from issuescout.cli.commands.dataset import (
    run as run_dataset,
)
from issuescout.cli.commands.scan import (
    run as run_scan,
)
from issuescout.cli.commands.version import (
    run as run_version,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="issuescout",
        description="IssueScout Command Line Interface",
    )

    subparsers = parser.add_subparsers(
        dest="command",
    )

    evaluate_parser = subparsers.add_parser(
        "evaluate",
        help="Run evaluation benchmarks",
    )

    evaluate_parser.add_argument(
        "dataset",
        help="Path to the evaluation dataset",
    )

    scan_parser = subparsers.add_parser(
        "scan",
        help="Scan a GitHub repository",
    )

    scan_parser.add_argument(
        "owner",
        help="Repository owner",
    )

    scan_parser.add_argument(
        "repository",
        help="Repository name",
    )

    scan_parser.add_argument(
        "--format",
        choices=[
            "console",
            "json",
        ],
        default="console",
        help="Output format",
    )

    dataset_parser = subparsers.add_parser(
        "dataset",
        help="Generate an evaluation dataset",
    )

    dataset_parser.add_argument(
        "owner",
        help="Repository owner",
    )

    dataset_parser.add_argument(
        "repository",
        help="Repository name",
    )

    dataset_parser.add_argument(
        "--limit",
        type=int,
        default=100,
        help="Maximum number of closed issues",
    )

    subparsers.add_parser(
        "version",
        help="Display version information",
    )

    return parser


def main() -> None:
    parser = build_parser()

    args = parser.parse_args()

    match args.command:
        case "evaluate":
            run_evaluate(
                args.dataset,
            )

        case "scan":
            run_scan(
                args.owner,
                args.repository,
                args.format,
            )

        case "dataset":
            run_dataset(
                args.owner,
                args.repository,
                args.limit,
            )

        case "version":
            run_version()

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
