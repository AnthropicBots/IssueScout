import json

import pytest

from issuescout.evaluation.loader import EvaluationLoader


def test_invalid_json(
    tmp_path,
):
    path = tmp_path / "dataset.json"

    path.write_text(
        "{invalid json",
        encoding="utf-8",
    )

    with pytest.raises(
        json.JSONDecodeError,
    ):
        EvaluationLoader().load(path)
