from __future__ import annotations

from pydantic import BaseModel


class ScanPlan(BaseModel):
    """
    Describes how a repository scan should be executed.
    """

    issue_limit: int = 100

    include_comments: bool = False

    include_timeline: bool = False

    include_closed_issues: bool = False

    continue_from_page: int = 1
