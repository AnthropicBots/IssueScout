from __future__ import annotations

from issuescout.evaluation.benchmark.repository import RepositoryBenchmark


class BenchmarkSuite:
    """
    Holds benchmark results for multiple repositories.
    """

    def __init__(self) -> None:
        self._benchmarks: list[RepositoryBenchmark] = []

    def add(
        self,
        benchmark: RepositoryBenchmark,
    ) -> None:
        self._benchmarks.append(benchmark)

    @property
    def benchmarks(
        self,
    ) -> list[RepositoryBenchmark]:
        return list(self._benchmarks)

    def __len__(
        self,
    ) -> int:
        return len(self._benchmarks)
