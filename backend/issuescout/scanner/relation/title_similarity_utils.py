from __future__ import annotations

from issuescout.utils.text_similarity import (
    similarity_percentage,
)


def normalized_title_similarity(
    left: str | None,
    right: str | None,
) -> int:
    """
    Returns a normalized similarity score between
    two titles.

    Thresholds are intentionally coarse so that
    very similar titles receive a stronger signal.
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
