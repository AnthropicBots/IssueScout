import logging
from issuescout.models import (
    Issue,
    RepositoryScanContext,
)

logger = logging.getLogger(__name__)


class AnalysisPipeline:
    def __init__(self, analyzers):
        self.analyzers = analyzers

    async def run(
        self,
        context: RepositoryScanContext,
        issue: Issue,
    ):
        results = []

        for analyzer in self.analyzers:
            try:
                result = await analyzer.analyze(
                    context,
                    issue,
                )
            except Exception:
                logger.exception(
                    "Analyzer '%s' failed.",
                    analyzer.__class__.__name__,
                )
                continue

            results.append(result)

        return results
