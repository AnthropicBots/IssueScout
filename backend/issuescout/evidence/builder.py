from __future__ import annotations

from .model import (
    EvidenceItem,
    EvidenceSummary,
)
from .weights import (
    EvidenceWeights,
)


class EvidenceBuilder:
    """
    Builds EvidenceSummary objects from individual
    evidence items.
    """

    def __init__(self) -> None:
        self._items: list[EvidenceItem] = []

    def add(
        self,
        *,
        type: str,
        label: str,
        description: str,
        weight: int,
        passed: bool,
        details: dict[str, object] | None = None,
    ) -> "EvidenceBuilder":
        self._items.append(
            EvidenceItem(
                type=type,
                label=label,
                description=description,
                weight=weight,
                passed=passed,
                details=details or {},
            ),
        )
        return self

    def extend(
        self,
        items: list[EvidenceItem],
    ) -> "EvidenceBuilder":
        self._items.extend(items)
        return self

    def add_title_similarity(
        self,
        *,
        weight: int,
    ) -> "EvidenceBuilder":
        return self.add(
            type="title_similarity",
            label="Title Similarity",
            description=("Issue title matches the pull request title."),
            weight=weight,
            passed=True,
        )

    def add_body_similarity(
        self,
        *,
        weight: int,
        overlap: int,
    ) -> "EvidenceBuilder":
        return self.add(
            type="body_similarity",
            label="Body Similarity",
            description=("Issue and pull request bodies share significant content."),
            weight=weight,
            passed=True,
            details={
                "overlap": overlap,
            },
        )

    def add_merged(
        self,
    ) -> "EvidenceBuilder":
        return self.add(
            type="merged",
            label="Merged Pull Request",
            description="The pull request has been merged.",
            weight=EvidenceWeights.MERGED,
            passed=True,
        )

    def add_reviews(
        self,
        *,
        review_count: int,
    ) -> "EvidenceBuilder":
        return self.add(
            type="reviews",
            label="Pull Request Reviews",
            description="The pull request has received reviews.",
            weight=EvidenceWeights.REVIEWS,
            passed=True,
            details={
                "count": review_count,
            },
        )

    def add_discussion(
        self,
        *,
        comment_count: int,
    ) -> "EvidenceBuilder":
        return self.add(
            type="discussion",
            label="Discussion",
            description="The pull request contains discussion.",
            weight=EvidenceWeights.DISCUSSION,
            passed=True,
            details={
                "comments": comment_count,
            },
        )

    def add_commits(
        self,
        *,
        commit_count: int,
    ) -> "EvidenceBuilder":
        return self.add(
            type="commits",
            label="Commit History",
            description="The pull request contains commits.",
            weight=EvidenceWeights.COMMITS,
            passed=True,
            details={
                "count": commit_count,
            },
        )

    def add_changed_files(
        self,
        *,
        file_count: int,
    ) -> "EvidenceBuilder":
        return self.add(
            type="changed_files",
            label="Changed Files",
            description="The pull request modifies project files.",
            weight=EvidenceWeights.CHANGED_FILES,
            passed=True,
            details={
                "count": file_count,
            },
        )

    def add_discussion_intelligence(
        self,
        *,
        confidence: int,
    ) -> "EvidenceBuilder":
        return self.add(
            type="discussion_intelligence",
            label="Discussion Intelligence",
            description=("Positive resolution evidence detected in the discussion."),
            weight=confidence // 10,
            passed=True,
            details={
                "confidence": confidence,
            },
        )

    def build(self) -> EvidenceSummary:
        return EvidenceSummary(
            items=list(self._items),
        )

    def clear(self) -> "EvidenceBuilder":
        self._items.clear()
        return self
