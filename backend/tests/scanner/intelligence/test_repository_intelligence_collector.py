import pytest

from issuescout.models import Repository

from issuescout.scanner.intelligence.repository.collector import (
    RepositoryIntelligenceCollector,
)


@pytest.mark.anyio
async def test_collect_repository_intelligence():

    repository = Repository(
        owner="python",
        name="cpython",
        description="Python language",
        homepage="https://python.org",
        language="Python",
        default_branch="main",
        license_name="PSF",
        stars=100,
        forks=20,
        watchers=10,
        open_issues=5,
        archived=False,
        disabled=False,
        topics=[
            "python",
            "interpreter",
        ],
    )

    collector = RepositoryIntelligenceCollector()

    intelligence = await collector.collect(
        repository,
    )

    assert intelligence.owner == "python"
    assert intelligence.name == "cpython"
    assert intelligence.description == "Python language"
    assert intelligence.language == "Python"
    assert intelligence.license_name == "PSF"
    assert intelligence.stars == 100
    assert intelligence.forks == 20
    assert intelligence.watchers == 10
    assert intelligence.open_issues == 5
    assert intelligence.topics == [
        "python",
        "interpreter",
    ]


@pytest.mark.anyio
async def test_collect_repository_with_defaults():

    repository = Repository(
        owner="owner",
        name="repo",
    )

    collector = RepositoryIntelligenceCollector()

    intelligence = await collector.collect(
        repository,
    )

    assert intelligence.owner == "owner"
    assert intelligence.name == "repo"
    assert intelligence.description is None
    assert intelligence.language is None
    assert intelligence.topics == []
