from issuescout.evaluation.pipeline import EvaluationPipeline


def test_pipeline_empty():
    summary = EvaluationPipeline().summarize([])

    assert summary.issue_count == 0
    assert summary.accuracy == 0.0
    assert summary.precision == 0.0
    assert summary.recall == 0.0
    assert summary.mrr == 0.0
    assert summary.map == 0.0
