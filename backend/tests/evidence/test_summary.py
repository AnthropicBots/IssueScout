from issuescout.evidence import (
    EvidenceBuilder,
)
from issuescout.evidence.summary import (
    failed,
    failed_weight,
    passed,
    passed_weight,
    total_weight,
)


def test_summary_helpers():

    summary = (
        EvidenceBuilder()
        .add(
            type="pass",
            label="Pass",
            description="",
            weight=20,
            passed=True,
        )
        .add(
            type="fail",
            label="Fail",
            description="",
            weight=10,
            passed=False,
        )
        .build()
    )

    assert len(passed(summary)) == 1
    assert len(failed(summary)) == 1

    assert total_weight(summary) == 30
    assert passed_weight(summary) == 20
    assert failed_weight(summary) == 10
