from __future__ import annotations

import re
from issuescout.utils.github_keywords import (
    CLOSING_KEYWORDS,
)

_PR_URL_PATTERN = re.compile(
    r"github\.com/[^/]+/[^/]+/pull/(\d+)",
    re.IGNORECASE,
)

_ISSUE_URL_PATTERN = re.compile(
    r"github\.com/[^/]+/[^/]+/issues/(\d+)",
    re.IGNORECASE,
)

_REFERENCE_PATTERN = re.compile(
    r"#(\d+)",
)

_CLOSING_KEYWORD_PATTERN = re.compile(
    r"\b(?:fix(?:e[sd])?|close(?:[sd])?|resolve(?:[sd])?)\s+#(\d+)",
    re.IGNORECASE,
)

_BACKPORT_PATTERN = re.compile(
    r"\bbackport\s+#(\d+)",
    re.IGNORECASE,
)

_CLOSING_REFERENCE_PATTERN = re.compile(
    (
        r"\b([a-z]+)"
        r"\s+"
        r"(?:[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)?"
        r"#(\d+)"
    ),
    re.IGNORECASE,
)


def extract_pull_request_numbers(
    text: str | None,
) -> set[int]:
    """
    Extract pull request references from GitHub URLs.
    """

    if not text:
        return set()

    return {int(match) for match in _PR_URL_PATTERN.findall(text)}


def extract_issue_numbers(
    text: str | None,
) -> set[int]:
    """
    Extract issue references from GitHub URLs
    and #123 style references.
    """

    if not text:
        return set()

    references = {int(match) for match in _REFERENCE_PATTERN.findall(text)}

    references.update(int(match) for match in _ISSUE_URL_PATTERN.findall(text))

    for keyword, issue_number in _CLOSING_REFERENCE_PATTERN.findall(text):
        if keyword.lower() in CLOSING_KEYWORDS:
            references.add(int(issue_number))

    return references


def extract_candidate_pull_request_numbers(
    text: str | None,
) -> set[int]:
    """
    Extract pull request references from free-form text.

    Supports:

    - GitHub PR URLs
    - Fixes #123
    - Closes #123
    - Resolves #123
    - Backport #123
    """

    if not text:
        return set()

    references = set()

    references.update(
        extract_pull_request_numbers(
            text,
        )
    )

    references.update(
        int(match)
        for match in _CLOSING_KEYWORD_PATTERN.findall(
            text,
        )
    )

    references.update(
        int(match)
        for match in _BACKPORT_PATTERN.findall(
            text,
        )
    )

    return references
