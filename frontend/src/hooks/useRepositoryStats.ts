import { useMemo } from "react";

import type { IssueSummary } from "../types/api";

interface RepositoryStats {
  averageConfidence: number;
  assignedIssues: number;
  linkedPRs: number;
}

export function useRepositoryStats(
  issues: IssueSummary[],
): RepositoryStats {
  return useMemo(() => {
    const averageConfidence =
      issues.length === 0
        ? 0
        : Math.round(
            issues.reduce(
              (sum, issue) =>
                sum + issue.confidence,
              0,
            ) / issues.length,
          );

    return {
      averageConfidence,
      assignedIssues: issues.filter(
        (i) => i.assigned,
      ).length,
      linkedPRs: issues.filter(
        (i) => i.linked_pr_number,
      ).length,
    };
  }, [issues]);
}
