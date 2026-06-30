from __future__ import annotations

from issuescout.evaluation.dataset.builder import DatasetBuilder


def dataset() -> DatasetBuilder:
    """
    Create a dataset builder.
    """

    return DatasetBuilder()
