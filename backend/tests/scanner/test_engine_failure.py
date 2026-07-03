from issuescout.scanner.engine import ScannerEngine


def test_engine_creation():
    engine = ScannerEngine()

    assert engine is not None
    assert hasattr(engine, "scan_repository")
