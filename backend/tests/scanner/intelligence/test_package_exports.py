from issuescout.scanner.intelligence import (
    IssueIntelligence,
    RepositoryIntelligence,
)


def test_package_exports():

    assert IssueIntelligence.__name__ == "IssueIntelligence"

    assert RepositoryIntelligence.__name__ == "RepositoryIntelligence"
