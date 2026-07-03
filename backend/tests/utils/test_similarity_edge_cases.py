from issuescout.utils.text_similarity import similarity_percentage


def test_same_text():
    assert similarity_percentage("bug fix", "bug fix") == 100


def test_case_insensitive():
    assert similarity_percentage("Bug", "bug") == 100


def test_completely_different():
    assert similarity_percentage("abc", "xyz") < 50
