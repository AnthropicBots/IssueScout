from pathlib import Path

import pytest

from issuescout.evaluation.loader import EvaluationLoader


def test_missing_dataset():
    loader = EvaluationLoader()

    with pytest.raises(FileNotFoundError):
        loader.load(
            Path("missing.json"),
        )
