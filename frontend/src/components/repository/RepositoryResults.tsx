import type { ScanResult } from "../../types/api";

import EmptyState from "./EmptyState";
import IssueCard from "./IssueCard";
import RepositoryStats from "./RepositoryStats";
import SearchToolbar from "./SearchToolbar";

type Props = {
  result: ScanResult;
};

export default function RepositoryResults({
  result,
}: Props) {
  return (
    <div className="mt-8 space-y-8">
      <RepositoryStats
        repository={result.repository}
        totalIssues={result.total_issues}
        availableIssues={result.available_issues}
      />

      <SearchToolbar />

      {result.issues.length === 0 ? (
        <EmptyState />
      ) : (
        <div className="space-y-5">
          {result.issues.map((issue) => (
            <IssueCard
              key={issue.number}
              issue={issue}
            />
          ))}
        </div>
      )}
    </div>
  );
}
