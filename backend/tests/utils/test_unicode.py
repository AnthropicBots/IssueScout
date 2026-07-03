from issuescout.utils.text_similarity import similarity_percentage


def test_unicode_similarity():
    score = similarity_percentage(
        "résumé",
        "resume",
    )

    assert isinstance(score, int)


def test_emoji_similarity():
    score = similarity_percentage(
        "fix 🐛",
        "fix 🐛",
    )

    assert score == 100
