import { useState } from "react";
import type { ScanResult } from "../../types/api";
import { useFilters } from "../../hooks/useFilters";
import { useRepositoryStats } from "../../hooks/useRepositoryStats";
import { useSorting } from "../../hooks/useSorting";
import RepositoryOverview from "../dashboard/RepositoryOverview";
import EmptyState from "./EmptyState";
import IssueCard from "./IssueCard";
import SearchToolbar from "./SearchToolbar";

type Props = {
  result: ScanResult;
  owner: string;
  repo: string;
};

export default function RepositoryResults({
  result,
  owner,
  repo,
}: Props) {
  const [searchQuery, setSearchQuery] = useState("");
  const [sortBy, setSortBy] = useState("confidence-desc");
  const [filterBy, setFilterBy] = useState("all");

  const {
    averageConfidence,
  } = useRepositoryStats(result.issues);

  const filteredIssues = useFilters({
    issues: result.issues,
    searchQuery,
    filterBy,
  });

  const sortedIssues = useSorting({
    issues: filteredIssues,
    sortBy,
  });

  return (
    <div className="mt-10 space-y-8">

      <RepositoryOverview
        repository={result.repository}
        totalIssues={result.total_issues}
        availableIssues={result.available_issues}
        averageConfidence={averageConfidence}
      />

      <div className="rounded-2xl border border-slate-200 bg-gradient-to-r from-slate-50 to-blue-50 p-6 shadow-sm">
        <div className="grid gap-6 md:grid-cols-3">

          <div>
            <p className="text-sm font-medium uppercase tracking-wide text-slate-500">
              Scan Status
            </p>

            <h3 className="mt-2 text-xl font-bold text-green-600">
              Completed Successfully
            </h3>

            <p className="mt-2 text-sm text-slate-500">
              Repository analysis finished successfully.
            </p>
          </div>

          <div>
            <p className="text-sm font-medium uppercase tracking-wide text-slate-500">
              Issues Found
            </p>

            <h3 className="mt-2 text-xl font-bold text-slate-900">
              {result.total_issues}
            </h3>

            <p className="mt-2 text-sm text-slate-500">
              {result.available_issues} available for contribution.
            </p>
          </div>

          <div>
            <p className="text-sm font-medium uppercase tracking-wide text-slate-500">
              Prediction Quality
            </p>

            <h3 className="mt-2 text-xl font-bold text-blue-600">
              {averageConfidence}%
            </h3>

            <p className="mt-2 text-sm text-slate-500">
              Average prediction confidence.
            </p>
          </div>

        </div>
      </div>

      <SearchToolbar
        searchQuery={searchQuery}
        sortBy={sortBy}
        filterBy={filterBy}
        onSearchChange={setSearchQuery}
        onSortChange={setSortBy}
        onFilterChange={setFilterBy}
      />

      <div className="flex flex-col gap-3 rounded-2xl border border-slate-200 bg-white p-5 shadow-sm md:flex-row md:items-center md:justify-between">
        <div>
          <p className="text-lg font-semibold text-slate-900">
            Showing {sortedIssues.length} of {result.issues.length} issues
          </p>

          <p className="text-sm text-slate-500">
            Results update instantly as you search, filter, or sort.
          </p>
        </div>
        <div className="rounded-full bg-blue-100 px-4 py-2 text-sm font-semibold text-blue-700">
          {sortedIssues.length} Results
        </div>
      </div>

      {sortedIssues.length === 0 ? (
        <EmptyState />
      ) : (
        <div className="space-y-5">
          {sortedIssues.map((issue) => (
            <IssueCard
              key={issue.number}
              issue={issue}
              owner={owner}
              repo={repo}
            />
          ))}
        </div>
      )}
    </div>
  );
}
