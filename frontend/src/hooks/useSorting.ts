import { useMemo } from "react";

import type { IssueSummary } from "../types/api";

interface SortOptions {
  issues: IssueSummary[];
  sortBy: string;
}

export function useSorting({
  issues,
  sortBy,
}: SortOptions) {
  return useMemo(() => {
    const sorted = [...issues];

    switch (sortBy) {
      case "confidence-desc":
        sorted.sort(
          (a, b) =>
            b.confidence - a.confidence,
        );
        break;

      case "confidence-asc":
        sorted.sort(
          (a, b) =>
            a.confidence - b.confidence,
        );
        break;

      case "issue-desc":
        sorted.sort(
          (a, b) => b.number - a.number,
        );
        break;

      case "issue-asc":
        sorted.sort(
          (a, b) => a.number - b.number,
        );
        break;

      case "title":
        sorted.sort((a, b) =>
          a.title.localeCompare(b.title),
        );
        break;
    }

    return sorted;
  }, [issues, sortBy]);
}
