import pytest

from issuescout.models import (
    Repository,
    RepositoryScanContext,
)
from issuescout.scanner.pipeline import AnalysisPipeline

from tests.helpers.factories import (
    make_issue,
)


class FailingAnalyzer:
    async def analyze(
        self,
        context,
        issue,
    ):
        raise RuntimeError("failure")


@pytest.mark.anyio
async def test_pipeline_creation():
    pipeline = AnalysisPipeline([])

    assert pipeline is not None
    assert pipeline.analyzers == []


@pytest.mark.anyio
async def test_pipeline_skips_failed_analyzer():
    pipeline = AnalysisPipeline(
        [
            FailingAnalyzer(),
        ]
    )

    context = RepositoryScanContext(
        repository=Repository(
            owner="python",
            name="cpython",
        ),
    )

    results = await pipeline.run(
        context,
        make_issue(),
    )

    assert results == []
