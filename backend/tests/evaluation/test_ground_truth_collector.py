import pytest

from issuescout.evaluation.collector.collector import GroundTruthCollector


def test_ground_truth_collector_base():

    collector = GroundTruthCollector()

    with pytest.raises(
        NotImplementedError,
    ):
        collector.collect()
