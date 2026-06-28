from issuescout.models import (
    PullRequest,
    RepositoryScanContext,
)

from issuescout.scanner.detectors.linked_pr_detector import (
    LinkedPRDetector,
)

from issuescout.prediction import (
    PredictionService,
)

from issuescout.evidence import (
    EvidenceCollector,
)

from issuescout.scanner.relation import (
    RelationEngine,
    default_analyzers,
)

from issuescout.output import explain_prediction
from issuescout.presentation import (
    ConsoleReporter,
)

class GitHubLinkedPRDetector(LinkedPRDetector):
    """
    Detect linked pull requests using the
    already-fetched RepositoryScanContext.
    """

    def __init__(self):
        self.evidence_collector = EvidenceCollector()

        self.relation_engine = RelationEngine(
            default_analyzers(),
        )

        self.prediction_service = PredictionService(
            self.relation_engine,
        )
        self.console_reporter = ConsoleReporter()

    async def find_linked_pr(
        self,
        context: RepositoryScanContext,
        issue_number: int,
    ) -> PullRequest | None:
        
        issue = next(
            issue
            for issue in context.issues
            if issue.number == issue_number
        )

        await self.evidence_collector.collect(
            context,
            issue,
        )

        prediction = await self.prediction_service.predict(
            issue,
            context.pull_requests,
        )

        if prediction.prediction is None:
        
            return None

        self.console_reporter.report(
            prediction,
        )

        return prediction.prediction.pull_request
    
    async def close(self):
        await self.evidence_collector.close()