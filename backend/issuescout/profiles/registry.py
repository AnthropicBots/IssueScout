from __future__ import annotations

from issuescout.profiles.base import RepositoryProfile
from issuescout.profiles.cpython import CPythonProfile


class ProfileRegistry:
    """
    Registry of supported repositories.
    """

    def __init__(self) -> None:
        self._profiles = {
            "python/cpython": CPythonProfile(),
        }

    def get(
        self,
        full_name: str,
    ) -> RepositoryProfile | None:
        return self._profiles.get(full_name)

    def all(
        self,
    ) -> list[RepositoryProfile]:
        return list(self._profiles.values())
