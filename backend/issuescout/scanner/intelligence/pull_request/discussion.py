from __future__ import annotations


class PullRequestDiscussionAnalyzer:
    """
    Performs lightweight analysis of a pull request
    discussion to determine whether it contains
    evidence that the PR resolves an issue.
    """

    POSITIVE_KEYWORDS = (
        "fixes",
        "fixed",
        "closes",
        "closed",
        "resolves",
        "resolved",
        "backport",
        "approved",
        "approve",
        "lgtm",
        "merged",
    )

    NEGATIVE_KEYWORDS = (
        "changes requested",
        "request changes",
        "needs work",
        "not correct",
        "incorrect",
        "won't fix",
        "does not fix",
    )

    def analyze(
        self,
        text: str,
    ) -> dict[str, object]:

        lowered = text.lower()

        matched = [keyword for keyword in self.POSITIVE_KEYWORDS if keyword in lowered]

        approval_count = lowered.count(
            "approved",
        )

        merged = "merged" in lowered

        negative = [keyword for keyword in self.NEGATIVE_KEYWORDS if keyword in lowered]

        confidence = len(matched) * 20 + approval_count * 10 - len(negative) * 20

        confidence = max(
            0,
            min(confidence, 100),
        )

        return {
            "matched": bool(matched),
            "keywords": matched,
            "negative_keywords": negative,
            "confidence": confidence,
            "approval_count": approval_count,
            "merged": merged,
        }
