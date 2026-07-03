from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class RepositoryDTO:
    name: str
    owner: str
    stars: int
    forks: int
    open_issues: int
    default_branch: str
