from __future__ import annotations

import asyncio
from pathlib import Path
import json
from issuescout.evaluation.dataset.builder import DatasetBuilder
from issuescout.evaluation.dataset.generator import DatasetGenerator


def dataset(
    repository_owner: str,
    repository_name: str,
) -> DatasetBuilder:
    """
    Create a dataset builder for a repository.

    Preserved for backward compatibility.
    """

    return DatasetBuilder(
        repository_owner=repository_owner,
        repository_name=repository_name,
    )


async def _generate(
    repository_owner: str,
    repository_name: str,
    limit: int,
) -> None:
    """
    Generate an evaluation dataset and save it to disk.
    """

    generator = DatasetGenerator()

    try:
        print(f"Generating dataset for {repository_owner}/{repository_name}...")

        evaluation = await generator.generate(
            repository_owner,
            repository_name,
            limit=limit,
        )

        output_directory = Path("evaluation/datasets")
        output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path = (
            output_directory / f"{repository_owner}_{repository_name}_evaluation.json"
        )

        output_path.write_text(
            json.dumps(
                evaluation.to_dict(),
                indent=2,
            ),
            encoding="utf-8",
        )

        print(f"Dataset saved to: {output_path}")
        print(f"Records: {len(evaluation.records)}")

    finally:
        await generator.close()


def run(
    repository_owner: str,
    repository_name: str,
    limit: int,
) -> None:
    """
    Generate an evaluation dataset from the command line.
    """

    asyncio.run(
        _generate(
            repository_owner,
            repository_name,
            limit,
        )
    )
