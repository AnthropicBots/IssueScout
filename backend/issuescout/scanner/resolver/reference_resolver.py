from __future__ import annotations

import re


class ReferenceResolver:
    """
    Extracts referenced pull request numbers from
    arbitrary GitHub text.
    """

    _pattern = re.compile(
        r"(?:#|GH-)(\d+)",
        re.IGNORECASE,
    )

    def resolve(
        self,
        text: str | None,
    ) -> set[int]:
        if not text:
            return set()

        return {int(match) for match in self._pattern.findall(text)}
