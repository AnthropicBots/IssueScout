from issuescout.scanner.fetcher import Fetcher


def test_fetcher_has_review_service():
    fetcher = Fetcher()

    assert fetcher.review_service is not None
