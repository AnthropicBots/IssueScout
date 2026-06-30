from __future__ import annotations

from issuescout.profiles.base import RepositoryProfile


class CPythonProfile(RepositoryProfile):
    @property
    def owner(self) -> str:
        return "python"

    @property
    def repository(self) -> str:
        return "cpython"

    @property
    def default_branch(self) -> str:
        return "main"
