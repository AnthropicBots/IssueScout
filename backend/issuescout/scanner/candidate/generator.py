from __future__ import annotations

from issuescout.models import (
    Issue,
    PullRequest,
)


class CandidateGenerator:
    """
    Generates candidate pull requests for an issue.

    This stage intentionally casts a wide net. Later
    stages are responsible for scoring and filtering
    the candidates.
    """

    def generate(
        self,
        issue: Issue,
        pull_requests: list[PullRequest],
    ) -> list[PullRequest]:
        return pull_requests.copy()
