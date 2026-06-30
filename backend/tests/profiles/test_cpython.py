from issuescout.profiles.cpython import CPythonProfile


def test_cpython_profile():

    profile = CPythonProfile()

    assert profile.owner == "python"

    assert profile.repository == "cpython"

    assert profile.full_name == "python/cpython"
