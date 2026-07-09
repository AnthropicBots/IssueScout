from __future__ import annotations

from .discussion import PullRequestDiscussionAnalyzer


class PullRequestDiscussionCollector:
    """
    Collects textual evidence from a pull request.
    """

    def __init__(self) -> None:
        self.analyzer = PullRequestDiscussionAnalyzer()

    def collect(
        self,
        body: str,
        comments: list[str],
    ) -> dict[str, object]:

        discussion = "\n".join(
            [
                body,
                *comments,
            ]
        )

        return self.analyzer.analyze(
            discussion,
        )
