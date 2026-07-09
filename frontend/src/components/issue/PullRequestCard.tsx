import {
  ArrowRight,
  CheckCircle2,
  GitPullRequest,
  Link2Off,
} from "lucide-react";

import Card from "../ui/Card";

interface PullRequestCardProps {
  number?: number | null;
  title?: string | null;
}

export default function PullRequestCard({
  number,
  title,
}: PullRequestCardProps) {
  const hasPullRequest = Boolean(number);

  return (
    <Card className="overflow-hidden rounded-[1.75rem] border border-slate-200 shadow-sm transition-all duration-300 hover:shadow-lg">
      <div className="space-y-6">
        {/* Header */}

        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div
              className={`flex h-12 w-12 items-center justify-center rounded-2xl ${
                hasPullRequest
                  ? "bg-green-100 text-green-600"
                  : "bg-slate-100 text-slate-500"
              }`}
            >
              {hasPullRequest ? (
                <GitPullRequest size={22} />
              ) : (
                <Link2Off size={22} />
              )}
            </div>

            <div>
              <h3 className="text-xl font-bold text-slate-900">
                Linked Pull Request
              </h3>

              <p className="text-sm text-slate-500">
                Relationship detected by IssueScout
              </p>
            </div>
          </div>

          {hasPullRequest && (
            <div className="rounded-full bg-green-100 px-4 py-2 text-sm font-semibold text-green-700">
              Linked
            </div>
          )}
        </div>

        {/* Content */}

        {hasPullRequest ? (
          <div className="rounded-2xl border border-green-200 bg-green-50 p-6">
            <div className="flex items-center gap-2">
              <CheckCircle2
                size={20}
                className="text-green-600"
              />

              <span className="text-sm font-semibold uppercase tracking-wide text-green-700">
                Pull Request Found
              </span>
            </div>

            <h4 className="mt-4 text-3xl font-black text-slate-900">
              #{number}
            </h4>

            {title && (
              <p className="mt-3 leading-7 text-slate-600">
                {title}
              </p>
            )}

            <div className="mt-6 inline-flex items-center gap-2 rounded-full bg-white px-4 py-2 text-sm font-semibold text-blue-600 shadow-sm">
              View Pull Request
              <ArrowRight size={16} />
            </div>
          </div>
        ) : (
          <div className="rounded-2xl border border-dashed border-slate-300 bg-slate-50 p-8 text-center">
            <div className="mx-auto mb-4 flex h-16 w-16 items-center justify-center rounded-full bg-slate-100">
              <Link2Off
                size={28}
                className="text-slate-500"
              />
            </div>

            <h4 className="text-xl font-bold text-slate-900">
              No Linked Pull Request
            </h4>

            <p className="mt-3 max-w-md mx-auto leading-7 text-slate-600">
              IssueScout could not identify a pull request
              that is confidently related to this issue.
              This issue may still be open for new
              contributors.
            </p>
          </div>
        )}
      </div>
    </Card>
  );
}
