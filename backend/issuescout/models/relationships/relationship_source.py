from __future__ import annotations

from enum import StrEnum


class RelationshipSource(StrEnum):
    """
    Origin of a discovered relationship.
    """

    ISSUE_BODY = "issue_body"

    ISSUE_COMMENT = "issue_comment"

    ISSUE_TIMELINE = "issue_timeline"

    PULL_REQUEST_BODY = "pull_request_body"

    PULL_REQUEST_COMMENT = "pull_request_comment"

    REVIEW = "review"

    REVIEW_COMMENT = "review_comment"

    COMMIT_MESSAGE = "commit_message"

    COMMIT_BODY = "commit_body"

    TIMELINE_EVENT = "timeline_event"

    UNKNOWN = "unknown"
