from issuescout.evaluation.dataset.builder import DatasetBuilder
from issuescout.evaluation.models import (
    EvaluationRecord,
    GroundTruthRecord,
)


def make_record() -> EvaluationRecord:
    return EvaluationRecord(
        ground_truth=GroundTruthRecord(
            repository_owner="python",
            repository_name="cpython",
            issue_number=1,
            issue_title="Issue",
            issue_state="closed",
            actual_pull_request=10,
        ),
    )


def test_builder_creates_dataset():
    builder = DatasetBuilder(
        repository_owner="python",
        repository_name="cpython",
    )

    builder.add_record(
        make_record(),
    )

    dataset = builder.build()

    assert dataset.repository_owner == "python"
    assert dataset.repository_name == "cpython"
    assert len(dataset.records) == 1


def test_builder_empty_dataset():
    builder = DatasetBuilder(
        repository_owner="python",
        repository_name="cpython",
    )

    dataset = builder.build()

    assert dataset.records == []
