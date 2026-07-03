import asyncio

from issuescout.models import (
    IssueSummary,
    ScanResult,
)

from issuescout.scanner.fetcher import Fetcher
from issuescout.scanner.pipeline import AnalysisPipeline

from issuescout.scanner.analyzers import (
    AssignmentAnalyzer,
    LinkedPRAnalyzer,
)

from issuescout.scanner.detectors import (
    GitHubLinkedPRDetector,
)
from issuescout.scanner.confidence import ConfidenceCalculator
from issuescout.scanner.progress import ProgressCallback


class ScannerEngine:
    def __init__(
        self,
        fetcher: Fetcher | None = None,
        detector: GitHubLinkedPRDetector | None = None,
        pipeline: AnalysisPipeline | None = None,
        confidence: ConfidenceCalculator | None = None,
    ):
        self.fetcher = fetcher or Fetcher()

        self.detector = detector or GitHubLinkedPRDetector()

        self.pipeline = pipeline or AnalysisPipeline(
            [
                AssignmentAnalyzer(),
                LinkedPRAnalyzer(),
            ]
        )

        self.confidence = confidence or ConfidenceCalculator()

    async def _detect_linked_pr(
        self,
        context,
        issue,
    ):
        try:
            linked_pr = await self.detector.find_linked_pr(
                context,
                issue.number,
            )
        except Exception:
            linked_pr = None

        return issue.number, linked_pr

    async def scan_repository(
        self,
        owner: str,
        repo: str,
        progress_callback: ProgressCallback | None = None,
    ) -> ScanResult:

        context = await self.fetcher.fetch_context(
            owner,
            repo,
        )

        try:
            issues = context.issues

            processed = 0
            total = len(issues)

            if progress_callback is not None:
                progress_callback(
                    processed,
                    total,
                )

            results = await asyncio.gather(
                *[
                    self._detect_linked_pr(
                        context,
                        issue,
                    )
                    for issue in issues
                ]
            )

            for issue_number, linked_pr in results:
                context.linked_pr_cache[issue_number] = linked_pr

            summaries = []

            for issue in issues:
                results = await self.pipeline.run(
                    context,
                    issue,
                )

                print("=" * 80)
                print(f"Issue #{issue.number}: {issue.title}")

                for result in results:
                    print(
                        f"{result.analyzer}: "
                        f"passed={result.passed}, "
                        f"score={result.score}, "
                        f"reason={result.reason}"
                    )

                if not all(result.passed for result in results):
                    print("FILTERED")
                    continue

                print("KEPT")

                linked_pr = context.linked_pr_cache.get(
                    issue.number,
                )

                summaries.append(
                    IssueSummary(
                        number=issue.number,
                        title=issue.title,
                        assigned=issue.assigned,
                        assignee=issue.assignee,
                        confidence=self.confidence.calculate(
                            issue,
                            results,
                        ),
                        linked_pr_number=(
                            linked_pr.number if linked_pr is not None else None
                        ),
                        linked_pr_title=(
                            linked_pr.title if linked_pr is not None else None
                        ),
                    )
                )

                processed += 1

                if progress_callback is not None:
                    progress_callback(
                        processed,
                        total,
                    )
            print("=" * 80)
            print(f"Fetched issues : {len(issues)}")
            print(f"Returned issues: {len(summaries)}")
            print("=" * 80)

            return ScanResult(
                repository=f"{owner}/{repo}",
                total_issues=len(summaries),
                available_issues=len(summaries),
                issues=summaries,
            )

        finally:
            await self.fetcher.close()
            await self.detector.close()
