from issuescout.scanner.pipeline import AnalysisPipeline


def test_pipeline_creation():
    pipeline = AnalysisPipeline([])

    assert pipeline is not None
    assert pipeline.analyzers == []
