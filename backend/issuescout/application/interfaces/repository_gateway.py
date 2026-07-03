from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class RepositoryGateway(ABC):
    @abstractmethod
    async def get_repository(
        self,
        owner: str,
        repository: str,
    ) -> dict:
        """
        Retrieve repository metadata.
        """

    @abstractmethod
    async def close(self) -> None:
        """
        Release underlying resources.
        """
