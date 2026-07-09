from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class EvidenceItem:
    """
    Represents a single piece of evidence used when determining
    whether a pull request resolves an issue.
    """

    type: str
    label: str
    description: str
    weight: int
    passed: bool
    details: dict[str, object] = field(default_factory=dict)


@dataclass(slots=True)
class EvidenceSummary:
    """
    Collection of evidence produced during analysis.
    """

    items: list[EvidenceItem] = field(default_factory=list)

    @property
    def total_weight(self) -> int:
        return sum(item.weight for item in self.items)

    @property
    def passed_weight(self) -> int:
        return sum(item.weight for item in self.items if item.passed)

    @property
    def failed_weight(self) -> int:
        return self.total_weight - self.passed_weight

    @property
    def passed_items(self) -> list[EvidenceItem]:
        return [item for item in self.items if item.passed]

    @property
    def failed_items(self) -> list[EvidenceItem]:
        return [item for item in self.items if not item.passed]
