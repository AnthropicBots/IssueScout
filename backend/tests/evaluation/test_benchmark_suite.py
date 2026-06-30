from issuescout.evaluation.benchmark.repository import RepositoryBenchmark
from issuescout.evaluation.benchmark.suite import BenchmarkSuite
from issuescout.evaluation.metrics.summary import EvaluationSummary


def make_summary():
    return EvaluationSummary(
        issue_count=10,
        accuracy=0.9,
        precision=0.9,
        recall=0.9,
        mrr=0.95,
        map=0.95,
    )


def test_add_benchmark():
    suite = BenchmarkSuite()

    suite.add(
        RepositoryBenchmark(
            repository_owner="python",
            repository_name="cpython",
            summary=make_summary(),
        )
    )

    assert len(suite) == 1


def test_benchmark_collection():
    suite = BenchmarkSuite()

    suite.add(
        RepositoryBenchmark(
            repository_owner="python",
            repository_name="cpython",
            summary=make_summary(),
        )
    )

    suite.add(
        RepositoryBenchmark(
            repository_owner="django",
            repository_name="django",
            summary=make_summary(),
        )
    )

    assert len(suite.benchmarks) == 2
