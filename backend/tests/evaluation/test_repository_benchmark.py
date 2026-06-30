from issuescout.evaluation.benchmark.repository import RepositoryBenchmark
from issuescout.evaluation.metrics.summary import EvaluationSummary


def test_repository_full_name():
    benchmark = RepositoryBenchmark(
        repository_owner="python",
        repository_name="cpython",
        summary=EvaluationSummary(
            issue_count=10,
            accuracy=0.8,
            precision=0.8,
            recall=0.8,
            mrr=0.9,
            map=0.9,
        ),
    )

    assert benchmark.full_name == "python/cpython"
