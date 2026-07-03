from issuescout.evaluation.ground_truth import GroundTruthCollector


def test_parse_datetime_none():
    assert GroundTruthCollector._parse_datetime(None) is None


def test_parse_datetime_empty():
    assert GroundTruthCollector._parse_datetime("") is None


def test_parse_datetime_valid():
    value = GroundTruthCollector._parse_datetime(
        "2024-01-01T10:00:00Z",
    )

    assert value is not None
    assert value.year == 2024
