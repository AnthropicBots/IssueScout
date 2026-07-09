from __future__ import annotations

from issuescout.application.resolution.analysis_result import (
    ResolutionAnalysisResult,
)
from issuescout.domain.models import (
    CandidatePullRequestDetails,
)
from issuescout.evidence import (
    EvidenceBuilder,
    EvidenceWeights,
)


class ResolutionAnalyzer:
    """
    Estimates whether a pull request
    actually resolves an issue.
    """

    def analyze(
        self,
        issue_title: str,
        issue_body: str | None,
        candidate: CandidatePullRequestDetails,
    ) -> ResolutionAnalysisResult:

        confidence = 0

        reasons: list[str] = []

        passed: list[str] = []

        evidence = EvidenceBuilder()

        if issue_title.lower() in candidate.title.lower():
            confidence += EvidenceWeights.TITLE_SIMILARITY
            passed.append("title")

            evidence.add(
                type="title_similarity",
                label="Title Similarity",
                description="Issue title matches the pull request title.",
                weight=30,
                passed=True,
            )

        if issue_body:
            issue_words = set(
                issue_body.lower().split(),
            )

            body_words = set(
                candidate.body.lower().split(),
            )

            overlap = len(issue_words & body_words)

            if overlap >= 5:
                confidence += EvidenceWeights.BODY_SIMILARITY
                passed.append("body")
                reasons.append("Strong body similarity.")

                evidence.add(
                    type="body_similarity",
                    label="Body Similarity",
                    description=(
                        "Issue and pull request bodies share significant content."
                    ),
                    weight=30,
                    passed=True,
                    details={
                        "overlap": overlap,
                    },
                )

        if candidate.merged:
            confidence += EvidenceWeights.MERGED
            passed.append("merged")
            reasons.append("Pull request is merged.")

            evidence.add(
                type="merged",
                label="Merged Pull Request",
                description="The pull request has been merged.",
                weight=20,
                passed=True,
            )

        if candidate.review_count > 0:
            confidence += EvidenceWeights.REVIEWS
            passed.append("reviews")

            evidence.add(
                type="reviews",
                label="Pull Request Reviews",
                description="The pull request has received reviews.",
                weight=10,
                passed=True,
            )

        if candidate.changed_files:
            confidence += EvidenceWeights.CHANGED_FILES
            passed.append("files")
            reasons.append("Pull request changes project files.")

            evidence.add(
                type="changed_files",
                label="Changed Files",
                description=("The pull request modifies project files."),
                weight=10,
                passed=True,
                details={
                    "count": len(candidate.changed_files),
                },
            )

        if candidate.commits:
            confidence += EvidenceWeights.COMMITS
            passed.append("commits")
            reasons.append("Pull request contains commits.")

            evidence.add(
                type="commits",
                label="Commit History",
                description="The pull request contains commits.",
                weight=10,
                passed=True,
                details={
                    "count": len(candidate.commits),
                },
            )

        if candidate.comment_count > 0:
            confidence += EvidenceWeights.DISCUSSION
            passed.append("discussion")
            reasons.append("Pull request has discussion.")

            evidence.add(
                type="discussion",
                label="Discussion",
                description=("The pull request contains discussion."),
                weight=10,
                passed=True,
                details={
                    "comments": candidate.comment_count,
                },
            )

        if candidate.discussion_confidence > 0:
            confidence += candidate.discussion_confidence // 10

            passed.append(
                "review_discussion",
            )

            passed.append(
                "discussion_intelligence",
            )

            reasons.append("Discussion contains positive reviewer evidence.")

            reasons.append("Discussion contains positive resolution evidence.")

            evidence.add(
                type="discussion_intelligence",
                label="Discussion Intelligence",
                description=(
                    "Positive resolution evidence detected in the discussion."
                ),
                weight=(candidate.discussion_confidence // 10),
                passed=True,
                details={
                    "confidence": candidate.discussion_confidence,
                },
            )

        if confidence >= 80:
            verdict = "Very likely resolves issue"
        elif confidence >= 60:
            verdict = "Likely resolves issue"
        elif confidence >= 40:
            verdict = "Possibly related"
        else:
            verdict = "Unlikely"

        return ResolutionAnalysisResult(
            confidence=min(confidence, 100),
            reasons=reasons,
            passed_checks=passed,
            evidence=evidence.build(),
            verdict=verdict,
        )
