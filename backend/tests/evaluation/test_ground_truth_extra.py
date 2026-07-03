from issuescout.evaluation.ground_truth import GroundTruthCollector


def test_ground_truth_constructor():
    collector = GroundTruthCollector()

    assert collector is not None


def test_ground_truth_has_collect():
    collector = GroundTruthCollector()

    assert hasattr(collector, "collect")


def test_ground_truth_has_close():
    collector = GroundTruthCollector()

    assert hasattr(collector, "close")
