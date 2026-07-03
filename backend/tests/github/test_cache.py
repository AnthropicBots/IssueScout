from issuescout.github.cache import GitHubCache


def test_cache_store_and_get():
    cache = GitHubCache()

    cache.set("repo", {"id": 1})

    assert cache.get("repo") == {"id": 1}


def test_cache_returns_none():
    cache = GitHubCache()

    assert cache.get("missing") is None
