from issuescout.utils.issue_reference_parser import (
    extract_issue_references,
)


def test_empty_text():
    assert extract_issue_references("") == set()


def test_no_issue_reference():
    assert extract_issue_references("hello world") == set()


def test_duplicate_issue_reference():
    assert extract_issue_references(
        "Fixes #10 and fixes #10",
    ) == {10}
