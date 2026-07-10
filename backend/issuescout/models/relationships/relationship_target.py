from __future__ import annotations

from enum import StrEnum


class RelationshipTarget(StrEnum):
    """
    Type of GitHub object being referenced.
    """

    ISSUE = "issue"

    PULL_REQUEST = "pull_request"

    COMMIT = "commit"

    DISCUSSION = "discussion"

    UNKNOWN = "unknown"
