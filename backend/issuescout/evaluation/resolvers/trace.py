from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ResolutionStep:
    """
    Represents one decision taken by a resolver.
    """

    action: str

    message: str

    metadata: dict[str, str] = field(default_factory=dict)


@dataclass(slots=True)
class ResolutionTrace:
    """
    Stores the complete decision history of a resolver.

    This object is intended for debugging, benchmarking,
    UI explanations and future explainable AI features.
    """

    steps: list[ResolutionStep] = field(default_factory=list)

    def add(
        self,
        action: str,
        message: str,
        **metadata: str,
    ) -> None:
        self.steps.append(
            ResolutionStep(
                action=action,
                message=message,
                metadata=metadata,
            )
        )
