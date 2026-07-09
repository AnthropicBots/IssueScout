from issuescout.evidence import (
    EvidenceBuilder,
)


def test_build_empty_summary():

    summary = EvidenceBuilder().build()

    assert summary.items == []
    assert summary.total_weight == 0
    assert summary.passed_weight == 0
    assert summary.failed_weight == 0


def test_add_passed_evidence():

    summary = (
        EvidenceBuilder()
        .add(
            type="merged",
            label="Merged",
            description="PR merged.",
            weight=20,
            passed=True,
        )
        .build()
    )

    assert len(summary.items) == 1
    assert summary.total_weight == 20
    assert summary.passed_weight == 20
    assert summary.failed_weight == 0


def test_add_failed_evidence():

    summary = (
        EvidenceBuilder()
        .add(
            type="review",
            label="Changes Requested",
            description="Review requested changes.",
            weight=15,
            passed=False,
        )
        .build()
    )

    assert summary.total_weight == 15
    assert summary.failed_weight == 15
    assert summary.passed_weight == 0


def test_extend_builder():

    builder = EvidenceBuilder()

    builder.add(
        type="merged",
        label="Merged",
        description="Merged",
        weight=20,
        passed=True,
    )

    summary = builder.build()

    second = EvidenceBuilder().extend(summary.items).build()

    assert len(second.items) == 1


def test_domain_specific_builder_methods():

    summary = (
        EvidenceBuilder()
        .add_title_similarity(weight=30)
        .add_body_similarity(
            weight=30,
            overlap=8,
        )
        .add_merged()
        .add_reviews(
            review_count=2,
        )
        .add_discussion(
            comment_count=5,
        )
        .add_commits(
            commit_count=3,
        )
        .add_changed_files(
            file_count=6,
        )
        .add_discussion_intelligence(
            confidence=80,
        )
        .build()
    )

    assert len(summary.items) == 8

    assert summary.total_weight == 128
    assert summary.passed_weight == 128


def test_clear_builder():

    builder = EvidenceBuilder().add(
        type="merged",
        label="Merged",
        description="Merged",
        weight=20,
        passed=True,
    )

    builder.clear()

    summary = builder.build()

    assert summary.items == []


def test_add_defaults_details_to_empty_dict():

    summary = (
        EvidenceBuilder()
        .add(
            type="x",
            label="X",
            description="X",
            weight=1,
            passed=True,
        )
        .build()
    )

    assert summary.items[0].details == {}
