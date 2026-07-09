from pydantic import BaseModel, Field
from issuescout.evidence.model import (
    EvidenceItem,
)


class CandidatePullRequestSummary(BaseModel):
    number: int

    title: str

    confidence: int

    url: str

    sources: list[str]

    reasons: list[str]

    evidence: list[EvidenceItem] = Field(
        default_factory=list,
    )


class IssueSummary(BaseModel):
    number: int

    title: str

    assigned: bool

    assignee: str | None

    confidence: int

    linked_pr_number: int | None = None

    linked_pr_title: str | None = None

    candidate_count: int = 0

    candidate_pull_requests: list[CandidatePullRequestSummary] = Field(
        default_factory=list,
    )


class ScanResult(BaseModel):
    repository: str
    total_issues: int
    available_issues: int
    issues: list[IssueSummary]
