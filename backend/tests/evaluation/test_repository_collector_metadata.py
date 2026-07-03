from issuescout.evaluation.collector.repository import RepositoryCollector


def test_repository_property():
    collector = RepositoryCollector(
        "python",
        "cpython",
    )

    assert collector.repository == "python/cpython"
