from issuescout.scanner.engine import ScannerEngine


def test_engine_has_fetcher():
    engine = ScannerEngine()

    assert engine.fetcher is not None
