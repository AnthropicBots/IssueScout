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
from issuescout.scanner.candidate import (
    CandidateGenerator,
    CandidateResolver,
)
from issuescout.scanner.ranking import (
    CandidateRanker,
)
from issuescout.scanner.progress import ProgressCallback
from issuescout.scanner.planner import (
    ScanPlanner,
)
from issuescout.scanner.intelligence.repository import (
    RepositoryIntelligenceCollector,
)
from issuescout.scanner.candidate.pool import (
    CandidatePoolBuilder,
)
from issuescout.application.candidate.candidate_enricher import (
    CandidatePullRequestEnricher,
)
from issuescout.application.candidate_pull_request_service import (
    CandidatePullRequestService,
)
from issuescout.application.resolution import (
    ResolutionAnalyzer,
)
from issuescout.models.scan_result import (
    CandidatePullRequestSummary,
)


class ScannerEngine:
    def __init__(
        self,
        fetcher: Fetcher | None = None,
        detector: GitHubLinkedPRDetector | None = None,
        pipeline: AnalysisPipeline | None = None,
        confidence: ConfidenceCalculator | None = None,
        repository_intelligence: (RepositoryIntelligenceCollector | None) = None,
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
        self.candidate_generator = CandidateGenerator()
        self.candidate_resolver = CandidateResolver()
        self.candidate_ranker = CandidateRanker()
        self.planner = ScanPlanner()
        self.candidate_pool_builder = CandidatePoolBuilder()
        self.repository_intelligence = (
            repository_intelligence or RepositoryIntelligenceCollector()
        )
        self.candidate_discovery = CandidatePullRequestService()
        self.candidate_enricher = CandidatePullRequestEnricher()
        self.resolution_analyzer = ResolutionAnalyzer()

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

    async def _fetch_missing_pull_requests(
        self,
        *,
        owner: str,
        repo: str,
        context,
        resolved_pull_requests,
        missing_pull_requests,
    ) -> None:
        """
        Fetch candidate pull requests that were referenced but were not
        included in the initially fetched open pull requests.
        """

        for number in sorted(
            missing_pull_requests,
        ):
            if number in context.pull_request_lookup:
                continue

            try:
                pull_request = await self.fetcher.fetch_pull_request(
                    owner,
                    repo,
                    number,
                )

            except Exception:
                continue

            context.pull_request_lookup[number] = pull_request

            resolved_pull_requests.append(
                pull_request,
            )

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

        plan = self.planner.default_plan()

        issues = context.issues[: plan.issue_limit]

        context.repository_intelligence = await self.repository_intelligence.collect(
            context.repository,
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
                candidate_numbers = self.candidate_pool_builder.build(
                    issue,
                )

                context.candidate_pull_request_numbers = candidate_numbers

                resolved_pull_requests, missing_pull_requests = (
                    self.candidate_resolver.resolve(
                        candidate_numbers,
                        context.pull_request_lookup,
                    )
                )

                print(
                    "Missing candidate PRs:",
                    sorted(
                        missing_pull_requests,
                    ),
                )

                await self._fetch_missing_pull_requests(
                    owner=owner,
                    repo=repo,
                    context=context,
                    resolved_pull_requests=resolved_pull_requests,
                    missing_pull_requests=missing_pull_requests,
                )

                context.candidate_pull_requests = self.candidate_ranker.rank(
                    issue,
                    resolved_pull_requests,
                )
                results = await self.pipeline.run(
                    context,
                    issue,
                )

                print("=" * 80)
                print(f"Issue #{issue.number}: {issue.title}")
                print(
                    "Candidate PR references:",
                    sorted(
                        context.candidate_pull_request_numbers,
                    ),
                )
                print(
                    "Resolved candidates:",
                    [pr.number for pr in context.candidate_pull_requests],
                )

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

                linked_pr = (
                    context.candidate_pull_requests[0]
                    if context.candidate_pull_requests
                    else context.linked_pr_cache.get(
                        issue.number,
                    )
                )

                candidate_summaries: list[CandidatePullRequestSummary] = []

                discovered = await self.candidate_discovery.discover(
                    owner,
                    repo,
                    issue.number,
                    existing_numbers={
                        pr.number for pr in context.candidate_pull_requests
                    },
                )

                for candidate in discovered:
                    details = await self.candidate_enricher.enrich(
                        owner,
                        repo,
                        candidate,
                    )

                    analysis = self.resolution_analyzer.analyze(
                        issue.title,
                        issue.body,
                        details,
                    )

                    candidate_summaries.append(
                        CandidatePullRequestSummary(
                            number=details.number,
                            title=details.title,
                            confidence=analysis.confidence,
                            url=candidate.url,
                            sources=sorted(candidate.sources),
                            reasons=analysis.reasons,
                            evidence=analysis.evidence.items,
                        )
                    )

                candidate_summaries.sort(
                    key=lambda candidate: candidate.confidence,
                    reverse=True,
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
                        candidate_count=len(
                            candidate_summaries,
                        ),
                        candidate_pull_requests=candidate_summaries,
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
            await self.candidate_discovery.close()
            await self.candidate_enricher.close()
