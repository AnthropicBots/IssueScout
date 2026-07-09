from __future__ import annotations

from issuescout.scanner.planner.scan_plan import (
    ScanPlan,
)


class ScanPlanner:
    """
    Produces scan plans based on the
    requested scan strategy.
    """

    def default_plan(self) -> ScanPlan:
        return ScanPlan()
