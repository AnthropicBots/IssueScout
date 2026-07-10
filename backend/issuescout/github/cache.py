from __future__ import annotations

from collections import OrderedDict
from time import monotonic
from typing import Any

from issuescout.core.config import settings


class GitHubCache:
    """
    Simple in-memory cache with configurable TTL and maximum size.

    Expired entries are removed lazily during cache access. When the
    cache reaches its configured capacity, the oldest entry is evicted.
    """

    def __init__(self) -> None:
        self._cache: OrderedDict[
            str,
            tuple[float, Any],
        ] = OrderedDict()

    def get(
        self,
        key: str,
    ) -> Any | None:
        entry = self._cache.get(key)

        if entry is None:
            return None

        expires_at, value = entry

        if monotonic() >= expires_at:
            self._cache.pop(
                key,
                None,
            )
            return None

        self._cache.move_to_end(key)

        return value

    def set(
        self,
        key: str,
        value: Any,
    ) -> None:
        if key in self._cache:
            self._cache.move_to_end(key)

        elif len(self._cache) >= settings.CACHE_MAX_SIZE:
            self._cache.popitem(
                last=False,
            )

        self._cache[key] = (
            monotonic() + settings.CACHE_TTL,
            value,
        )

    def clear(
        self,
    ) -> None:
        self._cache.clear()

    def __contains__(
        self,
        key: str,
    ) -> bool:
        return self.get(key) is not None
