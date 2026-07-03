from issuescout.github.client import GitHubClient


def test_client_creation():
    client = GitHubClient()

    assert client is not None


def test_client_has_methods():
    client = GitHubClient()

    assert hasattr(client, "get")
    assert hasattr(client, "get_all")
    assert hasattr(client, "close")
