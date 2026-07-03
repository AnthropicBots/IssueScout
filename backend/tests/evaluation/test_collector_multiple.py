import pytest

from issuescout.evaluation.collector.collector import GroundTruthCollector


class SequenceCollector(GroundTruthCollector):
    async def collect(
        self,
        owner,
        repository,
        issue_number,
    ):
        return issue_number


@pytest.mark.anyio
async def test_collect_sequence():
    collector = SequenceCollector()

    results = []

    for number in (
        1,
        2,
        3,
    ):
        results.append(
            await collector.collect(
                "owner",
                "repo",
                number,
            )
        )

    assert results == [
        1,
        2,
        3,
    ]
