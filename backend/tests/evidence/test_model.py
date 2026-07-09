from issuescout.evidence.model import (
    EvidenceItem,
    EvidenceSummary,
)


def test_summary_properties():

    summary = EvidenceSummary(
        items=[
            EvidenceItem(
                type="a",
                label="A",
                description="",
                weight=20,
                passed=True,
            ),
            EvidenceItem(
                type="b",
                label="B",
                description="",
                weight=10,
                passed=False,
            ),
        ]
    )

    assert summary.total_weight == 30
    assert summary.passed_weight == 20
    assert summary.failed_weight == 10

    assert len(summary.passed_items) == 1
    assert len(summary.failed_items) == 1
