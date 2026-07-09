from __future__ import annotations

from issuescout.models import Repository


class RepositoryBuilder:
    """
    Builds Repository domain models from GitHub
    repository payloads.

    Sprint 2 intentionally maps only the fields
    currently present in the Repository model.
    Future iterations will enrich this mapping.
    """

    def build(
        self,
        repository: dict,
    ) -> Repository:
        license_info = repository.get("license")

        return Repository(
            owner=repository["owner"]["login"],
            name=repository["name"],
            description=repository.get("description"),
            homepage=repository.get("homepage"),
            license_name=(license_info["name"] if license_info is not None else None),
            language=repository.get("language"),
            default_branch=repository.get(
                "default_branch",
                "main",
            ),
            stars=repository.get(
                "stargazers_count",
                0,
            ),
            forks=repository.get(
                "forks_count",
                0,
            ),
            watchers=repository.get(
                "subscribers_count",
                0,
            ),
            open_issues=repository.get(
                "open_issues_count",
                0,
            ),
            archived=repository.get(
                "archived",
                False,
            ),
            disabled=repository.get(
                "disabled",
                False,
            ),
            topics=repository.get(
                "topics",
                [],
            ),
        )
