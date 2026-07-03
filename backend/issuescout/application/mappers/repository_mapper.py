from __future__ import annotations

from issuescout.application.dto import RepositoryDTO


class RepositoryMapper:
    @staticmethod
    def from_github(data: dict) -> RepositoryDTO:
        return RepositoryDTO(
            name=data["name"],
            owner=data["owner"]["login"],
            stars=data["stargazers_count"],
            forks=data["forks_count"],
            open_issues=data["open_issues_count"],
            default_branch=data["default_branch"],
        )
