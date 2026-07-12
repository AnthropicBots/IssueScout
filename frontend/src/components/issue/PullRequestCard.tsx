import {
  ArrowUpRight,
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
    <Card hover={false} className="border border-slate-200">

      {/* Header */}

      <div className="flex items-center justify-between">

        <div className="flex items-center gap-3">

          <div
            className={`flex h-11 w-11 items-center justify-center rounded-xl ${
              hasPullRequest
                ? "bg-green-100 text-green-600"
                : "bg-slate-100 text-slate-500"
            }`}
          >
            {hasPullRequest ? (
              <GitPullRequest size={20} />
            ) : (
              <Link2Off size={20} />
            )}
          </div>

          <div>

            <h3 className="text-lg font-bold text-slate-900">
              Pull Request Relationship
            </h3>

            <p className="text-sm text-slate-500">
              Repository relationship analysis
            </p>

          </div>

        </div>

        <span
          className={`rounded-full px-3 py-1 text-xs font-semibold ${
            hasPullRequest
              ? "bg-green-100 text-green-700"
              : "bg-slate-100 text-slate-600"
          }`}
        >
          {hasPullRequest ? "Linked" : "Not Found"}
        </span>

      </div>

      <div className="mt-6">

        {hasPullRequest ? (

          <div className="rounded-2xl border border-green-200 bg-green-50 p-5">

            <div className="flex items-center gap-2 text-green-700">

              <CheckCircle2 size={18} />

              <span className="font-semibold">
                Related Pull Request Detected
              </span>

            </div>

            <h2 className="mt-4 text-3xl font-black text-slate-900">
              PR #{number}
            </h2>

            {title && (
              <p className="mt-3 text-slate-600 leading-7">
                {title}
              </p>
            )}

            <div className="mt-5 flex items-center gap-2 text-sm font-semibold text-blue-600">

              <ArrowUpRight size={16} />

              View on GitHub

            </div>

          </div>

        ) : (

          <div className="rounded-2xl border border-dashed border-slate-300 bg-slate-50 p-6">

            <div className="flex items-center gap-3">

              <div className="rounded-xl bg-white p-3 shadow-sm">

                <Link2Off
                  size={22}
                  className="text-slate-500"
                />

              </div>

              <div>

                <h4 className="font-bold text-slate-900">
                  No Official Pull Request
                </h4>

                <p className="mt-1 text-sm text-slate-600">
                  IssueScout did not detect an officially linked pull
                  request for this issue.
                </p>

              </div>

            </div>

            <div className="mt-5 rounded-xl bg-blue-50 p-4">

              <p className="text-sm text-slate-700">

                💡 This does <strong>not</strong> necessarily mean that no
                related pull request exists. It may still be referenced in
                comments, timeline events or discussions and can appear as a
                predicted relationship.

              </p>

            </div>

          </div>

        )}

      </div>

    </Card>
  );
}
