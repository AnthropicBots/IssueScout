from __future__ import annotations

from issuescout.models import (
    Issue,
    PullRequest,
)


class RelationshipScorer:
    """
    Computes a relationship score between
    an issue and a pull request.
    """

    def score(
        self,
        issue: Issue,
        pull_request: PullRequest,
    ) -> int:

        score = 0

        if pull_request.number in issue.body_pull_requests:
            score += 3

        if pull_request.number in issue.comment_pull_requests:
            score += 3

        if pull_request.number in issue.timeline_pull_requests:
            score += 5

        if pull_request.number in issue.commit_pull_requests:
            score += 4

        shared_files = issue.mentioned_files & pull_request.changed_files

        score += len(shared_files) * 2

        return score
