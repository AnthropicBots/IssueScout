import pytest

from issuescout.evaluation.collector.collector import GroundTruthCollector


class DuplicateCollector(GroundTruthCollector):
    async def collect(
        self,
        owner,
        repository,
        issue_number,
    ):
        return issue_number


@pytest.mark.anyio
async def test_collect_multiple_calls():
    collector = DuplicateCollector()

    first = await collector.collect(
        "owner",
        "repo",
        10,
    )

    second = await collector.collect(
        "owner",
        "repo",
        10,
    )

    assert first == second == 10
