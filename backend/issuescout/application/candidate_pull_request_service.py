from __future__ import annotations

from issuescout.domain.models import (
    CandidatePullRequest,
)
from issuescout.services.comment_service import (
    CommentService,
)
from issuescout.services.issue_service import (
    IssueService,
)
from issuescout.services.timeline_service import (
    TimelineService,
)
from issuescout.scanner.relationships import (
    RelationshipEngine,
)
from issuescout.models.relationships import (
    RelationshipTarget,
)
from issuescout.utils.github_reference_parser import (
    extract_candidate_pull_request_numbers,
)


class CandidatePullRequestService:
    """
    Discovers pull requests that may resolve
    an issue.
    """

    def __init__(self) -> None:
        self.issue_service = IssueService()
        self.comment_service = CommentService()
        self.timeline_service = TimelineService()

        self.relationships = RelationshipEngine()

    async def discover(
        self,
        owner: str,
        repository: str,
        issue_number: int,
        existing_numbers: set[int] | None = None,
    ) -> list[CandidatePullRequest]:

        issue = await self.issue_service.get_issue(
            owner,
            repository,
            issue_number,
        )

        comments = await self.comment_service.get_comments(
            owner,
            repository,
            issue_number,
        )

        timeline = await self.timeline_service.get_issue_timeline(
            owner,
            repository,
            issue_number,
        )

        discovered: dict[int, set[str]] = {}

        existing_numbers = existing_numbers or set()

        relationships = self.relationships.collect(
            body=issue.get("body"),
            comments=comments,
            timeline=timeline,
        )

        for relationship in relationships:
            if relationship.target == RelationshipTarget.ISSUE:
                continue

            discovered.setdefault(
                relationship.number,
                set(),
            ).add(
                relationship.source.value,
            )

        #
        # Backwards compatibility.
        #
        # Keep the legacy extraction until the
        # new relationship engine fully replaces it.
        #

        self._collect(
            discovered,
            issue.get("body") or "",
            "body",
        )

        for comment in comments:
            self._collect(
                discovered,
                comment.get("body") or "",
                "comment",
            )

        for event in timeline:
            self._collect_from_timeline_event(
                discovered,
                event,
            )

            self._collect(
                discovered,
                str(event),
                "timeline",
            )

        return [
            CandidatePullRequest(
                number=number,
                url=(f"https://github.com/{owner}/{repository}/pull/{number}"),
                sources=sources,
            )
            for number, sources in sorted(
                discovered.items(),
            )
            if number not in existing_numbers
        ]

    def _collect_from_timeline_event(
        self,
        discovered: dict[int, set[str]],
        event: dict,
    ) -> None:
        """
        Collect pull request references from structured
        GitHub timeline events.
        """

        source = event.get("source")

        if not isinstance(source, dict):
            return

        issue = source.get("issue")

        if not isinstance(issue, dict):
            return

        pull_request = issue.get("pull_request")

        if not isinstance(pull_request, dict):
            return

        number = issue.get("number")

        if isinstance(number, int):
            discovered.setdefault(
                number,
                set(),
            ).add("timeline")

    def _collect(
        self,
        discovered: dict[int, set[str]],
        text: str,
        source: str,
    ) -> None:

        for number in extract_candidate_pull_request_numbers(
            text,
        ):
            discovered.setdefault(
                number,
                set(),
            ).add(source)

    async def close(self) -> None:
        await self.issue_service.close()
        await self.comment_service.close()
        await self.timeline_service.close()
