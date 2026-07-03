from issuescout.scanner.pipeline import AnalysisPipeline


class DummyAnalyzer:
    async def analyze(
        self,
        context,
        issue,
    ):
        return "ok"


def test_pipeline_stores_analyzers():
    analyzer = DummyAnalyzer()

    pipeline = AnalysisPipeline(
        [
            analyzer,
        ]
    )

    assert len(pipeline.analyzers) == 1
    assert pipeline.analyzers[0] is analyzer
