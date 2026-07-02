from __future__ import annotations

from issuescout.evaluation.benchmark import BenchmarkSuite


def benchmark() -> BenchmarkSuite:
    """
    Create an empty benchmark suite.

    Repository benchmarks can be added by the evaluation pipeline or
    future CLI commands.
    """

    return BenchmarkSuite()
