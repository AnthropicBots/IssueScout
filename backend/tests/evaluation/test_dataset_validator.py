from issuescout.evaluation.dataset.builder import DatasetBuilder
from issuescout.evaluation.dataset.validator import DatasetValidator
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


def test_validator_accepts_valid_dataset():
    builder = DatasetBuilder(
        repository_owner="python",
        repository_name="cpython",
    )

    builder.add_record(
        make_record(),
    )

    validator = DatasetValidator()

    assert validator.is_valid(
        builder.build(),
    )


def test_validator_rejects_empty_dataset():
    builder = DatasetBuilder(
        repository_owner="python",
        repository_name="cpython",
    )

    validator = DatasetValidator()

    assert not validator.is_valid(
        builder.build(),
    )


def test_validator_reports_errors():
    builder = DatasetBuilder(
        repository_owner="",
        repository_name="",
    )

    validator = DatasetValidator()

    errors = validator.validate(
        builder.build(),
    )

    assert len(errors) == 3
