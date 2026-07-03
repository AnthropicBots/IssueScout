import type { IssueSummary } from "../../types/api";

import Badge from "../ui/Badge";
import Card from "../ui/Card";

type Props = {
  issue: IssueSummary;
};

function confidenceColor(
  confidence: number,
): "green" | "yellow" | "red" {
  if (confidence >= 80) {
    return "green";
  }

  if (confidence >= 50) {
    return "yellow";
  }

  return "red";
}

export default function IssueCard({
  issue,
}: Props) {
  return (
    <Card>
      <div className="flex flex-col gap-5 md:flex-row md:justify-between">
        <div className="space-y-3">
          <h3 className="text-xl font-semibold">
            #{issue.number} {issue.title}
          </h3>

          <div className="flex flex-wrap gap-3">
            <Badge color={confidenceColor(issue.confidence)}>
              Confidence {issue.confidence}%
            </Badge>

            <Badge color={issue.assigned ? "green" : "red"}>
              {issue.assigned ? "Assigned" : "Unassigned"}
            </Badge>
          </div>

          <div className="space-y-1 text-sm text-slate-600">
            <p>
              <span className="font-medium">
                Assignee:
              </span>{" "}
              {issue.assignee ?? "Not Assigned"}
            </p>

            <p>
              <span className="font-medium">
                Linked PR:
              </span>{" "}
              {issue.linked_pr_number
                ? `#${issue.linked_pr_number}`
                : "No linked pull request"}
            </p>

            {issue.linked_pr_title && (
              <p>
                <span className="font-medium">
                  PR Title:
                </span>{" "}
                {issue.linked_pr_title}
              </p>
            )}
          </div>
        </div>

        <div className="rounded-lg bg-slate-100 px-5 py-4 text-center">
          <p className="text-xs uppercase tracking-wide text-slate-500">
            Issue
          </p>

          <p className="text-2xl font-bold">
            #{issue.number}
          </p>
        </div>
      </div>
    </Card>
  );
}
