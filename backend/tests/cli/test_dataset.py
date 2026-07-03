from __future__ import annotations

import importlib
from pathlib import Path

dataset = importlib.import_module(
    "issuescout.cli.commands.dataset",
)


class FakeEvaluation:
    records = [1, 2]

    def to_dict(self):
        return {
            "records": self.records,
        }


class FakeGenerator:
    async def generate(
        self,
        owner,
        repository,
        limit=100,
    ):
        return FakeEvaluation()

    async def close(self):
        return None


def test_dataset_generation(
    monkeypatch,
    tmp_path,
):
    monkeypatch.chdir(tmp_path)

    monkeypatch.setattr(
        dataset,
        "DatasetGenerator",
        FakeGenerator,
    )

    dataset.run(
        "owner",
        "repo",
        5,
    )

    output = Path("evaluation") / "datasets" / "owner_repo_evaluation.json"

    assert output.exists()
