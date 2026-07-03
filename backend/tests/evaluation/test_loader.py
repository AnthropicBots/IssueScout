from issuescout.evaluation.loader import EvaluationLoader


def test_loader_instance():
    loader = EvaluationLoader()

    assert loader is not None


def test_loader_has_load():
    loader = EvaluationLoader()

    assert hasattr(loader, "load")
