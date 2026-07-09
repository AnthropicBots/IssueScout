from __future__ import annotations

from issuescout.models import Repository
from issuescout.scanner.intelligence.models import (
    RepositoryIntelligence,
)


class RepositoryIntelligenceCollector:
    """
    Collects repository-level intelligence.

    This collector currently mirrors the available
    Repository model. Future iterations will enrich it
    with additional repository metadata.
    """

    async def collect(
        self,
        repository: Repository,
    ) -> RepositoryIntelligence:
        return RepositoryIntelligence(
            owner=repository.owner,
            name=repository.name,
            description=repository.description,
            homepage=repository.homepage,
            language=repository.language,
            default_branch=repository.default_branch,
            license_name=repository.license_name,
            stars=repository.stars,
            forks=repository.forks,
            watchers=repository.watchers,
            open_issues=repository.open_issues,
            archived=repository.archived,
            disabled=repository.disabled,
            topics=repository.topics,
        )
