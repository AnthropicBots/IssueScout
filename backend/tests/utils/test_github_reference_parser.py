from issuescout.utils.github_reference_parser import (
    extract_issue_numbers,
)
from issuescout.utils.github_reference_parser import (
    extract_candidate_pull_request_numbers,
)


def test_extract_closing_keywords():
    text = """
    Fixes #12
    Closes #30
    Resolves #50
    """

    assert extract_issue_numbers(text) == {
        12,
        30,
        50,
    }


def test_extract_duplicate_references():
    text = """
    Fixes #10

    See #10

    Closes #10
    """

    assert extract_issue_numbers(text) == {
        10,
    }


def test_extract_plain_references():
    text = """
    Related to #1

    See #2

    #3
    """

    assert extract_issue_numbers(text) == {
        1,
        2,
        3,
    }


def test_extract_empty():
    assert extract_issue_numbers("") == set()


def test_extract_cross_repository_closing_reference():
    text = """
    Closes python/cpython#12345

    Fixes angular/angular#789

    Resolves org/project#55
    """

    assert extract_issue_numbers(text) == {
        12345,
        789,
        55,
    }


def test_extract_fixes_keyword():

    assert extract_candidate_pull_request_numbers("Fixes #123") == {123}


def test_extract_closes_keyword():

    assert extract_candidate_pull_request_numbers("Closes #456") == {456}


def test_extract_resolves_keyword():

    assert extract_candidate_pull_request_numbers("Resolves #789") == {789}


def test_extract_backport_keyword():

    assert extract_candidate_pull_request_numbers("Backport #999") == {999}
