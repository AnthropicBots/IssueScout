from pathlib import Path
from unittest.mock import Mock

from issuescout.application.evaluation_service import (
    ApplicationEvaluationService,
)


class FakeRepository:
    def __init__(self):
        self.records = ["r1", "r2"]


def test_evaluate_dataset():
    loader = Mock()
    runner = Mock()
    pipeline = Mock()

    repository = FakeRepository()

    loader.load.return_value = repository
    runner.run.return_value = ["comparison"]
    pipeline.summarize.return_value = "summary"

    service = ApplicationEvaluationService(
        runner=runner,
        loader=loader,
        pipeline=pipeline,
    )

    result = service.evaluate_dataset(
        Path("dataset.json"),
    )

    assert result == "summary"

    loader.load.assert_called_once()
    runner.run.assert_called_once_with(repository.records)
    pipeline.summarize.assert_called_once_with(["comparison"])


def test_summarize():
    runner = Mock()
    loader = Mock()
    pipeline = Mock()

    runner.run.return_value = ["comparison"]
    pipeline.summarize.return_value = "summary"

    service = ApplicationEvaluationService(
        runner=runner,
        loader=loader,
        pipeline=pipeline,
    )

    records = ["a", "b"]

    result = service.summarize(records)

    assert result == "summary"

    runner.run.assert_called_once_with(records)
    pipeline.summarize.assert_called_once_with(["comparison"])
