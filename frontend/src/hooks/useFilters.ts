import { useMemo } from "react";

import type { IssueSummary } from "../types/api";

interface FilterOptions {
  issues: IssueSummary[];
  searchQuery: string;
  filterBy: string;
}

export function useFilters({
  issues,
  searchQuery,
  filterBy,
}: FilterOptions) {
  return useMemo(() => {
    let filtered = [...issues];

    if (searchQuery.trim()) {
      const query = searchQuery.toLowerCase();

      filtered = filtered.filter(
        (issue) =>
          issue.title.toLowerCase().includes(query) ||
          issue.number
            .toString()
            .includes(query),
      );
    }

    switch (filterBy) {
      case "assigned":
        filtered = filtered.filter(
          (i) => i.assigned,
        );
        break;

      case "unassigned":
        filtered = filtered.filter(
          (i) => !i.assigned,
        );
        break;

      case "linked":
        filtered = filtered.filter(
          (i) => i.linked_pr_number,
        );
        break;

      case "unlinked":
        filtered = filtered.filter(
          (i) => !i.linked_pr_number,
        );
        break;
    }

    return filtered;
  }, [issues, searchQuery, filterBy]);
}
