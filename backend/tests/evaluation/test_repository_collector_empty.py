from issuescout.evaluation.collector.repository import RepositoryCollector


def test_build_empty_dataset():
    collector = RepositoryCollector(
        "owner",
        "repo",
    )

    dataset = collector.build_dataset([])

    assert dataset.records == []
