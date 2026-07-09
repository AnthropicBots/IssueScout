import pytest

from issuescout.models import (
    Repository,
    RepositoryScanContext,
)
from issuescout.scanner.pipeline import AnalysisPipeline

from tests.helpers.factories import (
    make_issue,
)


class DummyAnalyzer:
    async def analyze(
        self,
        context,
        issue,
    ):
        return "ok"


@pytest.mark.anyio
async def test_pipeline_stores_analyzers():
    analyzer = DummyAnalyzer()

    pipeline = AnalysisPipeline(
        [
            analyzer,
        ]
    )

    assert len(pipeline.analyzers) == 1
    assert pipeline.analyzers[0] is analyzer


@pytest.mark.anyio
async def test_pipeline_runs_single_analyzer():
    analyzer = DummyAnalyzer()

    pipeline = AnalysisPipeline(
        [
            analyzer,
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
        "ok",
    ]
