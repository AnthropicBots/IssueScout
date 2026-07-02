from __future__ import annotations

from typing import Protocol


class ProgressCallback(Protocol):
    """
    Callback invoked whenever repository scan progress changes.
    """

    def __call__(
        self,
        processed: int,
        total: int,
    ) -> None: ...
