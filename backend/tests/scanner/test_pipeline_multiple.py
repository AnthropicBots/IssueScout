from issuescout.scanner.pipeline import AnalysisPipeline


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


def test_pipeline_multiple_analyzers():
    pipeline = AnalysisPipeline(
        [
            AnalyzerA(),
            AnalyzerB(),
        ]
    )

    assert len(pipeline.analyzers) == 2
