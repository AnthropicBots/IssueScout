from __future__ import annotations

from issuescout.domain.models import (
    CandidatePullRequest,
    CandidatePullRequestDetails,
)
from issuescout.services.pull_request_service import (
    PullRequestService,
)

from issuescout.core.exceptions import (
    GitHubNotFoundError,
)
from issuescout.scanner.intelligence.pull_request import (
    PullRequestDiscussionCollector,
)
from typing import cast


class CandidatePullRequestEnricher:
    """
    Downloads detailed information
    for candidate pull requests.
    """

    def __init__(self) -> None:
        self.pull_request_service = PullRequestService()
        self.discussion = PullRequestDiscussionCollector()

    async def enrich(
        self,
        owner: str,
        repository: str,
        candidate: CandidatePullRequest,
    ) -> CandidatePullRequestDetails | None:

        try:
            pull_request = await self.pull_request_service.get_pull_request(
                owner,
                repository,
                candidate.number,
            )

        except GitHubNotFoundError:
            #
            # Candidate PR disappeared.
            #
            # This commonly happens when:
            #
            # • issue references a deleted PR
            # • history rewrite
            # • force push
            # • stale timeline reference
            #
            # Continue scanning the repository.
            #
            return None

        files = await self.pull_request_service.get_pull_request_files(
            owner,
            repository,
            candidate.number,
        )

        try:
            commits = await self.pull_request_service.get_pull_request_commits(
                owner,
                repository,
                candidate.number,
            )
        except Exception:
            commits = []

        reviews = await self.pull_request_service.get_pull_request_reviews(
            owner,
            repository,
            candidate.number,
        )

        review_comments = await self.pull_request_service.get_pull_request_comments(
            owner,
            repository,
            candidate.number,
        )

        discussion = self.discussion.collect(
            body=pull_request.get("body") or "",
            comments=[comment.get("body", "") for comment in review_comments],
        )

        return CandidatePullRequestDetails(
            number=pull_request["number"],
            title=pull_request["title"],
            body=pull_request.get("body") or "",
            state=pull_request["state"],
            merged=pull_request.get("merged", False),
            author=pull_request["user"]["login"],
            labels={label["name"] for label in pull_request["labels"]},
            changed_files={file["filename"] for file in files},
            commits=[commit["commit"]["message"] for commit in commits],
            review_count=len(reviews),
            comment_count=len(review_comments),
            discussion_keywords=cast(
                list[str],
                discussion["keywords"],
            ),
            discussion_confidence=cast(
                int,
                discussion["confidence"],
            ),
        )

    async def close(self) -> None:
        await self.pull_request_service.close()
