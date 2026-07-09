from issuescout.scanner.relation.body_similarity_utils import (
    normalized_body_similarity,
)


def test_identical_bodies():
    assert (
        normalized_body_similarity(
            "Fix parser crash",
            "Fix parser crash",
        )
        == 100
    )


def test_empty_body():
    assert (
        normalized_body_similarity(
            "",
            "Anything",
        )
        == 0
    )


def test_different_bodies():
    assert (
        normalized_body_similarity(
            "Parser crash",
            "Dark mode support",
        )
        < 40
    )
