from issuescout.scanner.engine import ScannerEngine


def test_engine_creation():
    engine = ScannerEngine()

    assert engine is not None


def test_engine_has_scan_repository():
    engine = ScannerEngine()

    assert hasattr(engine, "scan_repository")
