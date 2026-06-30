from issuescout.evaluation.collector.repository import RepositoryCollector


def test_repository_collector():

    collector = RepositoryCollector(
        "python",
        "cpython",
    )

    assert collector.repository_owner == "python"

    assert collector.repository_name == "cpython"
