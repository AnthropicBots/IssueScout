from __future__ import annotations

from issuescout.models import (
    Issue,
    PullRequest,
)
from issuescout.scanner.evidence import (
    RelationshipEvidenceCollector,
)
from issuescout.scanner.relationship import (
    RelationshipScorer,
)
from issuescout.scanner.relation.title_similarity_utils import (
    normalized_title_similarity,
)
from issuescout.scanner.relation.body_similarity_utils import (
    normalized_body_similarity,
)


class CandidateRanker:
    """
    Ranks candidate pull requests using
    relationship evidence.
    """

    def __init__(self) -> None:
        self.evidence = RelationshipEvidenceCollector()
        self.relationship_scorer = RelationshipScorer()

    def rank(
        self,
        issue: Issue,
        candidates: list[PullRequest],
    ) -> list[PullRequest]:
        scored: list[tuple[int, PullRequest]] = []

        for candidate in candidates:
            evidence = self.evidence.collect(
                issue,
                candidate,
            )

            score = self.relationship_scorer.score(
                issue,
                candidate,
            )

            score += int(evidence["reference_count"])

            score += (
                normalized_title_similarity(
                    issue.title,
                    candidate.title,
                )
                // 20
            )

            score += (
                normalized_body_similarity(
                    issue.body,
                    candidate.body,
                )
                // 25
            )

            scored.append(
                (
                    score,
                    candidate,
                )
            )

        scored.sort(
            key=lambda item: item[0],
            reverse=True,
        )

        return [candidate for _, candidate in scored]
