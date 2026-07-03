import {
  ArrowRight,
  CheckCircle2,
  GitPullRequest,
  User,
} from "lucide-react";

import {
  confidenceColor,
  formatConfidence,
} from "../../utils/formatters/formatConfidence";

import ConfidenceBar from "../issue/ConfidenceBar";
import { useNavigate } from "react-router-dom";
import Badge from "../ui/Badge";
import Card from "../ui/Card";

type Props = {
  issue: IssueSummary;
  owner: string;
  repo: string;
};

export default function IssueCard({
  issue,
  owner,
  repo,
}: Props) {
  const navigate = useNavigate();
  return (
    <Card
      className="cursor-pointer transition-all duration-300 hover:-translate-y-1 hover:shadow-xl"
      onClick={() =>
        navigate(
          `/${owner}/${repo}/issues/${issue.number}`,
          {
            state: {
              issue,
              owner,
              repo,
            },
          },
        )
      }
    >
      <div className="space-y-6">

        {/* Header */}
        <div className="flex flex-col gap-4 lg:flex-row lg:items-start lg:justify-between">

          <div className="space-y-3 flex-1">

            <div className="flex flex-wrap items-center gap-3">

              <span className="rounded-lg bg-slate-100 px-3 py-1 text-sm font-semibold text-slate-700">
                #{issue.number}
              </span>

              <Badge
                color={confidenceColor(issue.confidence)}
              >
                {formatConfidence(issue.confidence)} Confidence
              </Badge>

              <Badge
                color={issue.assigned ? "green" : "red"}
              >
                {issue.assigned
                  ? "Assigned"
                  : "Unassigned"}
              </Badge>

            </div>

            <h3 className="text-2xl font-bold leading-snug text-slate-900">
              {issue.title}
            </h3>

          </div>

          <ArrowRight
            size={22}
            className="text-slate-400"
          />

        </div>

        {/* Confidence */}
        <ConfidenceBar value={issue.confidence} />

        {/* Information */}
        <div className="grid gap-4 md:grid-cols-2">

          <div className="rounded-xl bg-slate-50 p-4">

            <div className="mb-2 flex items-center gap-2 font-semibold text-slate-700">
              <User size={18} />
              Assignee
            </div>

            <p className="text-slate-600">
              {issue.assignee ?? "Not Assigned"}
            </p>

          </div>

          <div className="rounded-xl bg-slate-50 p-4">

            <div className="mb-2 flex items-center gap-2 font-semibold text-slate-700">
              <GitPullRequest size={18} />
              Linked Pull Request
            </div>

            {issue.linked_pr_number ? (
              <>
                <p className="font-semibold">
                  #{issue.linked_pr_number}
                </p>

                {issue.linked_pr_title && (
                  <p className="mt-1 text-sm text-slate-500">
                    {issue.linked_pr_title}
                  </p>
                )}
              </>
            ) : (
              <p className="text-slate-500">
                No linked pull request
              </p>
            )}

          </div>

        </div>

        {/* Footer */}

        <div className="flex flex-wrap items-center justify-between border-t pt-4">

          <div className="flex items-center gap-2 text-sm text-slate-500">

            <CheckCircle2
              size={16}
              className="text-green-500"
            />

            Ready for contribution analysis

          </div>

          <button
            type="button"
            onClick={(e) => {
              e.stopPropagation();

              navigate(
                `/${owner}/${repo}/issues/${issue.number}`,
                {
                  state: {
                    issue,
                    owner,
                    repo,
                  },
                },
              );
            }}
            className="rounded-lg bg-blue-600 px-5 py-2 text-sm font-medium text-white transition hover:bg-blue-700"
          >
            View Details →
          </button>

        </div>

      </div>
    </Card>
  );
}
