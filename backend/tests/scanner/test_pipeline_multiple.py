import pytest

from issuescout.models import (
    Repository,
    RepositoryScanContext,
)
from issuescout.scanner.pipeline import AnalysisPipeline

from tests.helpers.factories import (
    make_issue,
)


class AnalyzerA:
    async def analyze(
        self,
        context,
        issue,
    ):
        return "a"


class AnalyzerB:
    async def analyze(
        self,
        context,
        issue,
    ):
        return "b"


@pytest.mark.anyio
async def test_pipeline_multiple_analyzers():
    pipeline = AnalysisPipeline(
        [
            AnalyzerA(),
            AnalyzerB(),
        ]
    )

    assert len(pipeline.analyzers) == 2


@pytest.mark.anyio
async def test_pipeline_returns_all_results():
    pipeline = AnalysisPipeline(
        [
            AnalyzerA(),
            AnalyzerB(),
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

    assert results == [
        "a",
        "b",
    ]
