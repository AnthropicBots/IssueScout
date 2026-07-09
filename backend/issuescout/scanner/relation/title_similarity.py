from issuescout.models import (
    Issue,
    PullRequest,
)
from issuescout.prediction.reason_builder import (
    ReasonBuilder,
)
from issuescout.scanner.relation.title_similarity_utils import (
    normalized_title_similarity,
)

from .base import RelationAnalyzer
from .metadata import AnalyzerMetadata
from .result import RelationResult


class TitleSimilarityAnalyzer(RelationAnalyzer):
    metadata = AnalyzerMetadata(
        name="title_similarity",
        weight=25,
        description="Compares issue title with PR title.",
    )

    async def analyze(
        self,
        issue: Issue,
        pull_request: PullRequest,
    ) -> RelationResult:

        percentage = normalized_title_similarity(
            issue.title,
            pull_request.title,
        )

        score = self.scoring.score(
            self.metadata,
            percentage,
        )

        return RelationResult(
            analyzer="title_similarity",
            score=score,
            confidence=percentage,
            reason=ReasonBuilder.title_similarity(
                percentage,
            ),
            matched_issue_text=issue.title,
            matched_pr_text=pull_request.title,
            details={
                "similarity": percentage,
                "issue_title": issue.title,
                "pull_request_title": pull_request.title,
            },
        )
