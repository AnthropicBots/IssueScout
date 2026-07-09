from pydantic import BaseModel, Field

from issuescout.models.issue import Issue
from issuescout.models.pull_request import PullRequest
from issuescout.models.repository import Repository

from issuescout.scanner.intelligence.models import (
    RepositoryIntelligence,
)


class RepositoryScanContext(BaseModel):
    repository: Repository

    repository_intelligence: RepositoryIntelligence | None = None

    issues: list[Issue] = Field(default_factory=list)

    pull_requests: list[PullRequest] = Field(
        default_factory=list,
    )

    resolved_pull_requests: dict[int, PullRequest] = Field(
        default_factory=dict,
    )

    pull_request_lookup: dict[int, PullRequest] = Field(
        default_factory=dict,
    )

    candidate_pull_requests: list[PullRequest] = Field(
        default_factory=list,
    )

    linked_pr_cache: dict[int, PullRequest | None] = Field(
        default_factory=dict,
    )

    candidate_pull_request_numbers: set[int] = Field(
        default_factory=set,
    )
