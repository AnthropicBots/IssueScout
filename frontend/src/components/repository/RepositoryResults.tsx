import { useState } from "react";
import {
  CheckCircle2,
  BarChart3,
  FolderGit2,
} from "lucide-react";

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

  const { averageConfidence } = useRepositoryStats(
    result.issues,
  );

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
    <div className="mt-12 space-y-8">
      <RepositoryOverview
        repository={result.repository}
        totalIssues={result.total_issues}
        availableIssues={result.available_issues}
        averageConfidence={averageConfidence}
      />

      {/* Scan Summary */}

      <div className="overflow-hidden rounded-[2rem] border border-slate-200 bg-gradient-to-br from-white via-slate-50 to-blue-50 shadow-lg">
        <div className="grid gap-6 p-8 md:grid-cols-3">
          <div className="rounded-2xl border border-green-100 bg-green-50 p-6">
            <div className="mb-4 flex h-12 w-12 items-center justify-center rounded-xl bg-green-100">
              <CheckCircle2
                size={24}
                className="text-green-600"
              />
            </div>

            <p className="text-sm font-semibold uppercase tracking-wider text-slate-500">
              Scan Status
            </p>

            <h3 className="mt-2 text-2xl font-bold text-green-700">
              Completed
            </h3>

            <p className="mt-3 text-sm leading-6 text-slate-600">
              Repository analysis finished successfully and
              prediction results are ready.
            </p>
          </div>

          <div className="rounded-2xl border border-blue-100 bg-blue-50 p-6">
            <div className="mb-4 flex h-12 w-12 items-center justify-center rounded-xl bg-blue-100">
              <FolderGit2
                size={24}
                className="text-blue-600"
              />
            </div>

            <p className="text-sm font-semibold uppercase tracking-wider text-slate-500">
              Issues Found
            </p>

            <h3 className="mt-2 text-2xl font-bold text-slate-900">
              {result.total_issues}
            </h3>

            <p className="mt-3 text-sm leading-6 text-slate-600">
              {result.available_issues} issues are available
              for contributors.
            </p>
          </div>

          <div className="rounded-2xl border border-cyan-100 bg-cyan-50 p-6">
            <div className="mb-4 flex h-12 w-12 items-center justify-center rounded-xl bg-cyan-100">
              <BarChart3
                size={24}
                className="text-cyan-600"
              />
            </div>

            <p className="text-sm font-semibold uppercase tracking-wider text-slate-500">
              Average Confidence
            </p>

            <h3 className="mt-2 text-2xl font-bold text-cyan-700">
              {averageConfidence}%
            </h3>

            <p className="mt-3 text-sm leading-6 text-slate-600">
              Overall confidence across all analyzed issues.
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

      {/* Results Header */}

      <div className="flex flex-col gap-4 rounded-[1.5rem] border border-slate-200 bg-white p-6 shadow-sm md:flex-row md:items-center md:justify-between">
        <div>
          <p className="text-2xl font-bold text-slate-900">
            Repository Issues
          </p>

          <p className="mt-2 text-slate-500">
            Showing{" "}
            <span className="font-semibold text-slate-900">
              {sortedIssues.length}
            </span>{" "}
            of{" "}
            <span className="font-semibold text-slate-900">
              {result.issues.length}
            </span>{" "}
            analyzed issues.
          </p>
        </div>

        <div className="inline-flex items-center rounded-full border border-blue-200 bg-blue-50 px-5 py-2 text-sm font-semibold text-blue-700">
          {sortedIssues.length} Results
        </div>
      </div>

      {sortedIssues.length === 0 ? (
        <EmptyState />
      ) : (
        <div className="space-y-6">
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
