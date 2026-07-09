from __future__ import annotations

from issuescout.models import (
    PullRequest,
)


class CandidateResolver:
    """
    Resolves candidate pull requests already
    available in memory.
    """

    def resolve(
        self,
        candidate_numbers: set[int],
        lookup: dict[int, PullRequest],
    ) -> tuple[list[PullRequest], set[int]]:
        resolved: list[PullRequest] = []
        missing: set[int] = set()

        for number in sorted(candidate_numbers):
            pull_request = lookup.get(number)

            if pull_request is None:
                missing.add(number)
                continue

            resolved.append(
                pull_request,
            )

        return (
            resolved,
            missing,
        )
