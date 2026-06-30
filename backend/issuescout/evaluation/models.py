from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


# ---------------------------------------------------------------------------
# Prediction Models
# ---------------------------------------------------------------------------


@dataclass(slots=True)
class PredictionCandidate:
    """
    Represents a predicted pull request returned by IssueScout.
    """

    pull_request_number: int
    score: float
    confidence: str
    rank: int
    matched: bool = False

    def to_dict(self) -> dict:
        return {
            "pull_request_number": self.pull_request_number,
            "score": self.score,
            "confidence": self.confidence,
            "rank": self.rank,
            "matched": self.matched,
        }

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ) -> "PredictionCandidate":
        return cls(
            pull_request_number=data["pull_request_number"],
            score=data["score"],
            confidence=data["confidence"],
            rank=data["rank"],
            matched=data.get(
                "matched",
                False,
            ),
        )


# ---------------------------------------------------------------------------
# Ground Truth Models
# ---------------------------------------------------------------------------


@dataclass(slots=True)
class GroundTruthRecord:
    """
    Represents one verified Issue → Pull Request relationship.

    This is the canonical record used throughout the evaluation framework.
    """

    repository_owner: str
    repository_name: str

    issue_number: int
    issue_title: str

    issue_state: str

    actual_pull_request: int | None

    issue_created_at: datetime | None = None
    issue_closed_at: datetime | None = None

    pull_request_created_at: datetime | None = None
    pull_request_merged_at: datetime | None = None

    linkage_method: str = "unknown"

    metadata: dict[str, str] = field(default_factory=dict)

    @property
    def full_repository_name(self) -> str:
        return f"{self.repository_owner}/{self.repository_name}"

    def to_dict(self) -> dict:
        return {
            "repository_owner": self.repository_owner,
            "repository_name": self.repository_name,
            "issue_number": self.issue_number,
            "issue_title": self.issue_title,
            "issue_state": self.issue_state,
            "actual_pull_request": self.actual_pull_request,
            "issue_created_at": self.issue_created_at.isoformat()
            if self.issue_created_at
            else None,
            "issue_closed_at": self.issue_closed_at.isoformat()
            if self.issue_closed_at
            else None,
            "pull_request_created_at": self.pull_request_created_at.isoformat()
            if self.pull_request_created_at
            else None,
            "pull_request_merged_at": self.pull_request_merged_at.isoformat()
            if self.pull_request_merged_at
            else None,
            "linkage_method": self.linkage_method,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ) -> "GroundTruthRecord":
        return cls(
            repository_owner=data["repository_owner"],
            repository_name=data["repository_name"],
            issue_number=data["issue_number"],
            issue_title=data.get(
                "issue_title",
                "",
            ),
            issue_state=data.get(
                "issue_state",
                "closed",
            ),
            actual_pull_request=data.get(
                "actual_pull_request",
            ),
            issue_created_at=datetime.fromisoformat(data["issue_created_at"])
            if data.get("issue_created_at")
            else None,
            issue_closed_at=datetime.fromisoformat(data["issue_closed_at"])
            if data.get("issue_closed_at")
            else None,
            pull_request_created_at=datetime.fromisoformat(
                data["pull_request_created_at"]
            )
            if data.get("pull_request_created_at")
            else None,
            pull_request_merged_at=datetime.fromisoformat(
                data["pull_request_merged_at"]
            )
            if data.get("pull_request_merged_at")
            else None,
            linkage_method=data.get(
                "linkage_method",
                "unknown",
            ),
            metadata=data.get(
                "metadata",
                {},
            ),
        )


# ---------------------------------------------------------------------------
# Evaluation Models
# ---------------------------------------------------------------------------


@dataclass(slots=True)
class EvaluationRecord:
    """
    Stores the prediction results for one ground-truth record.
    """

    ground_truth: GroundTruthRecord

    predictions: list[PredictionCandidate] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "ground_truth": self.ground_truth.to_dict(),
            "predictions": [prediction.to_dict() for prediction in self.predictions],
        }

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ) -> "EvaluationRecord":
        return cls(
            ground_truth=GroundTruthRecord.from_dict(
                data["ground_truth"],
            ),
            predictions=[
                PredictionCandidate.from_dict(prediction)
                for prediction in data.get(
                    "predictions",
                    [],
                )
            ],
        )


@dataclass(slots=True)
class RepositoryEvaluation:
    """
    Stores all evaluation records belonging to a repository.
    """

    repository_owner: str

    repository_name: str

    records: list[EvaluationRecord] = field(default_factory=list)

    @property
    def full_name(self) -> str:
        return f"{self.repository_owner}/{self.repository_name}"

    def to_dict(self) -> dict:
        return {
            "repository_owner": self.repository_owner,
            "repository_name": self.repository_name,
            "records": [record.to_dict() for record in self.records],
        }

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ) -> "RepositoryEvaluation":
        return cls(
            repository_owner=data["repository_owner"],
            repository_name=data["repository_name"],
            records=[
                EvaluationRecord.from_dict(record)
                for record in data.get(
                    "records",
                    [],
                )
            ],
        )
