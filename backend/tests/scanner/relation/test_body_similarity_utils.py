from issuescout.scanner.relation.body_similarity_utils import (
    normalized_body_similarity,
)


def test_body_similarity_partial():
    score = normalized_body_similarity(
        "Crash in asyncio transport",
        "Fix asyncio transport crash",
    )

    assert score >= 60
