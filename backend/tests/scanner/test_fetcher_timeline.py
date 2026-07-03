from issuescout.scanner.fetcher import Fetcher


def test_fetcher_has_pull_request_builder():
    fetcher = Fetcher()

    assert fetcher.pull_request_builder is not None
