from issuescout.profiles.registry import ProfileRegistry


def test_registry():

    registry = ProfileRegistry()

    profile = registry.get(
        "python/cpython",
    )

    assert profile is not None

    assert profile.full_name == "python/cpython"
