import json
from issuescout.evaluation.loader import EvaluationLoader


def test_loader_instance():
    loader = EvaluationLoader()

    assert loader is not None


def test_loader_has_load():
    loader = EvaluationLoader()

    assert hasattr(loader, "load")


def test_loads_native_repository_evaluation_format(
    tmp_path,
):

    dataset = {
        "repository_owner": "python",
        "repository_name": "cpython",
        "records": [],
    }

    path = tmp_path / "native.json"

    path.write_text(
        json.dumps(dataset),
        encoding="utf-8",
    )

    result = EvaluationLoader().load(path)

    assert result.repository_owner == "python"
    assert result.repository_name == "cpython"
    assert result.records == []


def test_loads_legacy_dataset():

    dataset = {
        "repository": "python/cpython",
        "records": [],
    }

    import tempfile

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".json",
        delete=False,
        encoding="utf-8",
    ) as file:
        json.dump(
            dataset,
            file,
        )

        path = file.name

    result = EvaluationLoader().load(path)

    assert result.repository_owner == "python"
    assert result.repository_name == "cpython"
    assert result.records == []


def test_loads_legacy_dataset_without_owner(
    tmp_path,
):

    dataset = {
        "repository": "cpython",
        "records": [],
    }

    path = tmp_path / "legacy.json"

    path.write_text(
        json.dumps(dataset),
        encoding="utf-8",
    )

    result = EvaluationLoader().load(path)

    assert result.repository_owner == ""
    assert result.repository_name == "cpython"


def test_loads_prediction_candidates(
    tmp_path,
):

    dataset = {
        "repository": "python/cpython",
        "records": [
            {
                "issue_number": 10,
                "issue_title": "Fix bug",
                "actual_pull_request": 20,
                "predictions": [
                    {
                        "pull_request_number": 20,
                        "score": 98,
                        "confidence": 95,
                        "rank": 1,
                        "matched": True,
                    },
                ],
            },
        ],
    }

    path = tmp_path / "dataset.json"

    path.write_text(
        json.dumps(dataset),
        encoding="utf-8",
    )

    result = EvaluationLoader().load(path)

    assert len(result.records) == 1

    prediction = result.records[0].predictions[0]

    assert prediction.pull_request_number == 20
    assert prediction.score == 98
    assert prediction.confidence == 95
    assert prediction.rank == 1
    assert prediction.matched is True


def test_loads_ground_truth_defaults(
    tmp_path,
):

    dataset = {
        "repository": "python/cpython",
        "records": [
            {
                "issue_number": 5,
            },
        ],
    }

    path = tmp_path / "defaults.json"

    path.write_text(
        json.dumps(dataset),
        encoding="utf-8",
    )

    result = EvaluationLoader().load(path)

    ground_truth = result.records[0].ground_truth

    assert ground_truth.issue_title == ""
    assert ground_truth.issue_state == "closed"
    assert ground_truth.actual_pull_request is None
    assert ground_truth.linkage_method == "legacy_json"


def test_loads_multiple_records(
    tmp_path,
):

    dataset = {
        "repository": "python/cpython",
        "records": [
            {
                "issue_number": 1,
            },
            {
                "issue_number": 2,
            },
        ],
    }

    path = tmp_path / "multiple.json"

    path.write_text(
        json.dumps(dataset),
        encoding="utf-8",
    )

    result = EvaluationLoader().load(path)

    assert len(result.records) == 2

    assert result.records[0].ground_truth.issue_number == 1
    assert result.records[1].ground_truth.issue_number == 2
