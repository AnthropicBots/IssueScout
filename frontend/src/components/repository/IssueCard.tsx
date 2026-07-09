import {
  ArrowRight,
  CheckCircle2,
  GitPullRequest,
  User,
} from "lucide-react";
import { useNavigate } from "react-router-dom";

import {
  confidenceColor,
  formatConfidence,
} from "../../utils/formatters/formatConfidence";

import type { IssueSummary } from "../../types/api";

import ConfidenceBar from "../issue/ConfidenceBar";
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

  const openIssue = () => {
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
  };

  return (
    <Card
      onClick={openIssue}
      className="group cursor-pointer overflow-hidden rounded-[1.75rem] border border-slate-200 bg-white transition-all duration-300 hover:-translate-y-1 hover:border-blue-200 hover:shadow-2xl"
    >
      <div className="space-y-6 p-1">
        {/* Header */}

        <div className="flex flex-col gap-5 lg:flex-row lg:items-start lg:justify-between">
          <div className="min-w-0 flex-1 space-y-4">
            <div className="flex flex-wrap items-center gap-3">
              <span className="rounded-xl bg-slate-100 px-3 py-1.5 text-sm font-semibold text-slate-700">
                #{issue.number}
              </span>

              <Badge
                color={confidenceColor(issue.confidence)}
              >
                {formatConfidence(issue.confidence)} Confidence
              </Badge>

              <Badge
                color={
                  issue.assigned ? "green" : "red"
                }
              >
                {issue.assigned
                  ? "Assigned"
                  : "Unassigned"}
              </Badge>
            </div>

            <h3 className="text-2xl font-bold leading-snug tracking-tight text-slate-900 transition-colors group-hover:text-blue-700">
              {issue.title}
            </h3>
          </div>

          <div className="rounded-xl bg-slate-100 p-3 transition-all group-hover:bg-blue-100">
            <ArrowRight
              size={22}
              className="text-slate-500 transition-transform duration-300 group-hover:translate-x-1 group-hover:text-blue-600"
            />
          </div>
        </div>

        {/* Confidence */}

        <div className="rounded-2xl border border-slate-100 bg-slate-50 p-5">
          <div className="mb-3 flex items-center justify-between">
            <p className="text-sm font-semibold uppercase tracking-wide text-slate-500">
              Prediction Confidence
            </p>

            <span className="text-lg font-bold text-slate-900">
              {issue.confidence}%
            </span>
          </div>

          <ConfidenceBar value={issue.confidence} />
        </div>

        {/* Details */}

        <div className="grid gap-5 lg:grid-cols-2">
          <div className="rounded-2xl border border-slate-100 bg-slate-50 p-5 transition-colors group-hover:bg-white">
            <div className="mb-3 flex items-center gap-2 text-sm font-semibold uppercase tracking-wide text-slate-600">
              <User
                size={18}
                className="text-blue-600"
              />
              Assignee
            </div>

            <p className="text-base font-medium text-slate-900">
              {issue.assignee ?? "Not Assigned"}
            </p>
          </div>

          <div className="rounded-2xl border border-slate-100 bg-slate-50 p-5 transition-colors group-hover:bg-white">
            <div className="mb-3 flex items-center gap-2 text-sm font-semibold uppercase tracking-wide text-slate-600">
              <GitPullRequest
                size={18}
                className="text-violet-600"
              />
              Linked Pull Request
            </div>

            {issue.linked_pr_number ? (
              <>
                <p className="text-base font-semibold text-slate-900">
                  #{issue.linked_pr_number}
                </p>

                {issue.linked_pr_title && (
                  <p className="mt-2 line-clamp-2 text-sm leading-6 text-slate-500">
                    {issue.linked_pr_title}
                  </p>
                )}
              </>
            ) : (
              <p className="text-base text-slate-500">
                No linked pull request detected.
              </p>
            )}
          </div>
        </div>

        {/* Footer */}

        <div className="flex flex-col gap-4 border-t border-slate-100 pt-5 sm:flex-row sm:items-center sm:justify-between">
          <div className="flex items-center gap-2 text-sm text-slate-500">
            <CheckCircle2
              size={18}
              className="text-emerald-500"
            />

            <span>
              Ready for contribution analysis
            </span>
          </div>

          <button
            type="button"
            onClick={(e) => {
              e.stopPropagation();
              openIssue();
            }}
            className="inline-flex items-center justify-center gap-2 rounded-xl bg-blue-600 px-5 py-2.5 text-sm font-semibold text-white transition-all duration-200 hover:bg-blue-700 hover:shadow-lg"
          >
            View Analysis

            <ArrowRight size={16} />
          </button>
        </div>
      </div>
    </Card>
  );
}
