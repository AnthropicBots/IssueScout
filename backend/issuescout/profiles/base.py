from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class RepositoryProfile(ABC):
    """
    Describes a supported GitHub repository.
    """

    @property
    @abstractmethod
    def owner(self) -> str: ...

    @property
    @abstractmethod
    def repository(self) -> str: ...

    @property
    def full_name(self) -> str:
        return f"{self.owner}/{self.repository}"

    @property
    def default_branch(self) -> str:
        return "main"

    @property
    def supports_issue_linking(self) -> bool:
        return True

    def __str__(self) -> str:
        return self.full_name
