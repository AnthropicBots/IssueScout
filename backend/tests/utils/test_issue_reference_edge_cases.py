from issuescout.utils.issue_reference_parser import (
    extract_issue_references,
)


def test_multiple_issue_numbers():
    assert extract_issue_references(
        "Fixes #1 closes #2 resolves #3",
    ) == {1, 2, 3}


def test_invalid_numbers():
    assert (
        extract_issue_references(
            "# abc #",
        )
        == set()
    )


def test_repository_reference():
    assert extract_issue_references(
        "python/cpython#123",
    ) == {123}


def test_github_url_reference():
    assert extract_issue_references(
        "https://github.com/python/cpython/issues/456",
    ) == {456}


def test_gh_reference():
    assert extract_issue_references(
        "gh-789",
    ) == {789}
