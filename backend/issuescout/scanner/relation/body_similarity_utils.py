from __future__ import annotations

from issuescout.utils.text_similarity import (
    similarity_percentage,
)


def normalized_body_similarity(
    left: str | None,
    right: str | None,
) -> int:
    """
    Computes a normalized similarity score between
    two text bodies.
    """

    if not left or not right:
        return 0

    similarity = similarity_percentage(
        left,
        right,
    )

    if similarity >= 90:
        return 100

    if similarity >= 75:
        return 80

    if similarity >= 60:
        return 60

    if similarity >= 40:
        return 40

    return 0
