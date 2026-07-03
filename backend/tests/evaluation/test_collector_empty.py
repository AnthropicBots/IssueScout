import pytest

from issuescout.evaluation.collector.collector import GroundTruthCollector


class DummyCollector(GroundTruthCollector):
    async def collect(
        self,
        owner,
        repository,
        issue_number,
    ):
        return None


@pytest.mark.anyio
async def test_collect_returns_none():
    collector = DummyCollector()

    result = await collector.collect(
        "owner",
        "repo",
        1,
    )

    assert result is None
