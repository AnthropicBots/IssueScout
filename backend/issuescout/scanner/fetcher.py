from issuescout.models.issue import Issue
import asyncio
from issuescout.models.pull_request import PullRequest
from issuescout.models.scan_context import RepositoryScanContext
from issuescout.scanner.builders.pull_request_builder import PullRequestBuilder
from issuescout.scanner.builders.repository import (
    RepositoryBuilder,
)
from issuescout.services.issue_service import IssueService
from issuescout.services.pull_request_service import PullRequestService
from issuescout.services.repository_service import RepositoryService
from issuescout.utils.issue_file_parser import (
    extract_file_mentions,
)
from issuescout.services.review_service import (
    ReviewService,
)
from issuescout.services.commit_history_service import (
    CommitHistoryService,
)
from issuescout.services.comment_service import (
    CommentService,
)
from issuescout.services.timeline_service import (
    TimelineService,
)


class Fetcher:
    def __init__(self):
        self.issue_service = IssueService()
        self.repository_service = RepositoryService()
        self.pull_request_service = PullRequestService()
        self.review_service = ReviewService()
        self.commit_history_service = CommitHistoryService()
        self.comment_service = CommentService()
        self.timeline_service = TimelineService()
        self.pull_request_builder = PullRequestBuilder()
        self.repository_builder = RepositoryBuilder()

    async def fetch_repository(
        self,
        owner: str,
        repo: str,
    ):
        return await self.repository_service.get_repository(
            owner,
            repo,
        )

    async def _fetch_issue_comments(
        self,
        owner: str,
        repo: str,
        issue_number: int,
    ) -> list[dict]:
        return await self.comment_service.get_comments(
            owner,
            repo,
            issue_number,
        )

    async def _fetch_issue_timeline(
        self,
        owner: str,
        repo: str,
        issue_number: int,
    ) -> list[dict]:
        return await self.timeline_service.get_issue_timeline(
            owner,
            repo,
            issue_number,
        )

    async def fetch_open_issues(
        self,
        owner: str,
        repo: str,
    ):
        github_issues = await self.issue_service.list_open_issues(
            owner,
            repo,
        )

        comments, timelines = await asyncio.gather(
            asyncio.gather(
                *[
                    self._fetch_issue_comments(
                        owner,
                        repo,
                        issue["number"],
                    )
                    for issue in github_issues
                    if "pull_request" not in issue
                ]
            ),
            asyncio.gather(
                *[
                    self._fetch_issue_timeline(
                        owner,
                        repo,
                        issue["number"],
                    )
                    for issue in github_issues
                    if "pull_request" not in issue
                ]
            ),
        )

        issues = []

        comment_index = 0

        for issue in github_issues:
            # GitHub's Issues API also returns pull requests.
            # Skip them so IssueScout only analyzes real issues.
            if "pull_request" in issue:
                continue

            issue_comments = comments[comment_index]
            issue_timeline = timelines[comment_index]
            comment_index += 1

            issues.append(
                Issue(
                    number=issue["number"],
                    title=issue["title"],
                    body=issue.get("body"),
                    comments=issue_comments,
                    timeline_events=issue_timeline,
                    author=issue["user"]["login"],
                    assignee=(
                        issue["assignee"]["login"] if issue["assignee"] else None
                    ),
                    assigned=issue["assignee"] is not None,
                    state=issue["state"],
                    created_at=issue.get("created_at"),
                    updated_at=issue.get("updated_at"),
                    closed_at=issue.get("closed_at"),
                    milestone=(
                        issue["milestone"]["title"] if issue.get("milestone") else None
                    ),
                    labels={label["name"] for label in issue["labels"]},
                    mentioned_files=extract_file_mentions(
                        (issue.get("title") or "") + "\n" + (issue.get("body") or "")
                    ),
                )
            )

        return issues

    async def _build_pull_request(
        self,
        owner: str,
        repo: str,
        pull_request: dict,
    ) -> PullRequest:

        files, reviewers, commits, branch_commit_history = await asyncio.gather(
            self.pull_request_service.get_pull_request_files(
                owner,
                repo,
                pull_request["number"],
            ),
            self.review_service.get_reviewers(
                owner,
                repo,
                pull_request["number"],
            ),
            self.pull_request_service.get_pull_request_commits(
                owner,
                repo,
                pull_request["number"],
            ),
            self.commit_history_service.list_branch_commits(
                owner,
                repo,
                pull_request["head"]["ref"],
            ),
        )

        return self.pull_request_builder.build(
            pull_request,
            reviewers=reviewers,
            commits=commits,
            branch_commit_history=branch_commit_history,
            changed_files={file["filename"] for file in files},
        )

    async def fetch_pull_request(
        self,
        owner: str,
        repo: str,
        number: int,
    ) -> PullRequest:
        """
        Fetch and fully build a single pull request.
        """

        github_pull_request = await self.pull_request_service.get_pull_request(
            owner,
            repo,
            number,
        )

        return await self._build_pull_request(
            owner,
            repo,
            github_pull_request,
        )

    async def fetch_open_pull_requests(
        self,
        owner: str,
        repo: str,
    ):
        github_pull_requests = await self.pull_request_service.list_open_pull_requests(
            owner,
            repo,
        )

        return await asyncio.gather(
            *[
                self._build_pull_request(
                    owner,
                    repo,
                    pull_request,
                )
                for pull_request in github_pull_requests
            ]
        )

    async def fetch_context(
        self,
        owner: str,
        repo: str,
    ) -> RepositoryScanContext:

        repository_data, issues, pull_requests = await asyncio.gather(
            self.fetch_repository(
                owner,
                repo,
            ),
            self.fetch_open_issues(
                owner,
                repo,
            ),
            self.fetch_open_pull_requests(
                owner,
                repo,
            ),
        )

        repository = self.repository_builder.build(
            repository_data,
        )

        return RepositoryScanContext(
            repository=repository,
            issues=issues,
            pull_requests=pull_requests,
            pull_request_lookup={pr.number: pr for pr in pull_requests},
        )

    async def close(self):
        await self.issue_service.close()
        await self.repository_service.close()
        await self.pull_request_service.close()
        await self.review_service.close()
        await self.commit_history_service.close()
        await self.comment_service.close()
        await self.timeline_service.close()
