from __future__ import annotations

from issuescout.models import (
    Issue,
)


class CandidatePoolBuilder:
    """
    Builds the set of candidate pull request
    numbers discovered from every available
    source of evidence.
    """

    def build(
        self,
        issue: Issue,
    ) -> set[int]:

        return (
            issue.body_pull_requests
            | issue.comment_pull_requests
            | issue.timeline_pull_requests
            | issue.commit_pull_requests
        )
