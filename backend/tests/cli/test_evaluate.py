from __future__ import annotations

from issuescout.cli.commands.evaluate import (
    EvaluationCommand,
)


class FakeRepository:
    records = [1]


class FakeLoader:
    def load(
        self,
        path,
    ):
        return FakeRepository()


class FakeRunner:
    def run(
        self,
        records,
    ):
        return records


class FakeSummary:
    def to_dict(self):
        return {
            "accuracy": 1.0,
        }


class FakePipeline:
    def summarize(
        self,
        comparisons,
    ):
        return FakeSummary()


def test_evaluation_command():
    command = EvaluationCommand()

    command._loader = FakeLoader()
    command._runner = FakeRunner()
    command._pipeline = FakePipeline()

    summary = command.evaluate(
        "dataset.json",
    )

    assert summary.to_dict()["accuracy"] == 1.0
