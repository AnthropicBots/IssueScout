from issuescout.models.repository import Repository


def test_repository_model():
    repository = Repository(
        owner="python",
        name="cpython",
    )

    assert repository.owner == "python"
    assert repository.name == "cpython"
