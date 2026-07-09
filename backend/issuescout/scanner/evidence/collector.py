from __future__ import annotations

from issuescout.models import (
    Issue,
    PullRequest,
)


class RelationshipEvidenceCollector:
    """
    Collects relationship evidence between an
    issue and a candidate pull request.

    Later versions will combine body,
    comments, timeline events, commits,
    labels and file overlap.
    """

    def collect(
        self,
        issue: Issue,
        pull_request: PullRequest,
    ) -> dict[str, bool | int]:
        evidence: dict[str, bool | int] = {
            "body_reference": (pull_request.number in issue.body_pull_requests),
            "comment_reference": (pull_request.number in issue.comment_pull_requests),
            "timeline_reference": (pull_request.number in issue.timeline_pull_requests),
            "commit_reference": (pull_request.number in issue.commit_pull_requests),
        }

        evidence["reference_count"] = sum(bool(value) for value in evidence.values())

        return evidence
