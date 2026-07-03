from issuescout.evaluation.report import RepositoryMetrics


def test_repository_metrics_defaults():
    metrics = RepositoryMetrics()

    assert metrics.total_issues == 0
    assert metrics.evaluated_issues == 0
    assert metrics.top1_accuracy == 0.0
    assert metrics.top3_accuracy == 0.0
    assert metrics.top5_accuracy == 0.0
    assert metrics.mean_reciprocal_rank == 0.0
