from issuescout.github.auth import GitHubAuthentication


def test_environment_variable_name():

    assert GitHubAuthentication.ENVIRONMENT_VARIABLE == "GITHUB_TOKEN"


def test_configured_returns_bool():

    assert isinstance(
        GitHubAuthentication.configured(),
        bool,
    )
