from issuescout.utils.text_similarity import similarity_percentage


def test_empty_strings():
    assert similarity_percentage("", "") == 100


def test_one_empty_string():
    assert similarity_percentage("", "hello") == 0
    assert similarity_percentage("hello", "") == 0
