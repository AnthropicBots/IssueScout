from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class RepositoryMetrics:
    """
    Aggregate evaluation metrics for a single repository.
    """

    total_issues: int = 0

    evaluated_issues: int = 0

    top1_accuracy: float = 0.0

    top3_accuracy: float = 0.0

    top5_accuracy: float = 0.0

    precision_at_1: float = 0.0

    precision_at_3: float = 0.0

    precision_at_5: float = 0.0

    recall_at_1: float = 0.0

    recall_at_3: float = 0.0

    recall_at_5: float = 0.0

    mean_reciprocal_rank: float = 0.0

    mean_average_precision: float = 0.0

    f1_score: float = 0.0

    average_prediction_score: float = 0.0


@dataclass(slots=True)
class EvaluationFailure:
    """
    Represents one failed prediction.

    Stored separately so reports can explain
    why IssueScout failed.
    """

    issue_number: int

    actual_pull_request: int | None

    predicted_pull_request: int | None

    predicted_rank: int | None

    prediction_score: float | None

    reason: str = ""


@dataclass(slots=True)
class EvaluationReport:
    """
    Complete evaluation report.

    This object is independent of any output format.

    It can later be rendered as:

    - Markdown
    - HTML
    - JSON
    - PDF
    - Console
    """

    repository: str

    metrics: RepositoryMetrics = field(
        default_factory=RepositoryMetrics,
    )

    failures: list[EvaluationFailure] = field(
        default_factory=list,
    )

    metadata: dict[str, str] = field(
        default_factory=dict,
    )
