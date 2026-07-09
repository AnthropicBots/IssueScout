import {
  Brain,
  CheckCircle2,
  GitBranch,
  Loader2,
  Search,
} from "lucide-react";

interface LoadingStateProps {
  title?: string;
  description?: string;
}

export default function LoadingState({
  title = "Scanning Repository...",
  description = "IssueScout is analyzing issues, pull requests, and repository intelligence.",
}: LoadingStateProps) {
  return (
    <div className="overflow-hidden rounded-[2rem] border border-slate-200 bg-white shadow-lg">
      {/* Header */}

      <div className="border-b border-slate-100 bg-gradient-to-r from-blue-50 via-cyan-50 to-indigo-50 p-8">
        <div className="flex flex-col items-center text-center">
          <div className="flex h-20 w-20 items-center justify-center rounded-full bg-white shadow-lg">
            <Loader2
              size={42}
              className="animate-spin text-blue-600"
            />
          </div>

          <h2 className="mt-6 text-3xl font-black tracking-tight text-slate-900">
            {title}
          </h2>

          <p className="mt-4 max-w-2xl text-lg leading-8 text-slate-600">
            {description}
          </p>
        </div>
      </div>

      {/* Progress Steps */}

      <div className="space-y-5 p-8">
        <div className="flex items-center gap-4 rounded-2xl border border-slate-200 bg-slate-50 p-5">
          <div className="rounded-2xl bg-blue-100 p-3">
            <Search
              size={22}
              className="text-blue-600"
            />
          </div>

          <div className="flex-1">
            <h4 className="font-semibold text-slate-900">
              Fetching Repository
            </h4>

            <p className="mt-1 text-sm text-slate-600">
              Retrieving repository metadata and open
              issues from GitHub.
            </p>
          </div>

          <Loader2
            size={18}
            className="animate-spin text-blue-600"
          />
        </div>

        <div className="flex items-center gap-4 rounded-2xl border border-slate-200 bg-slate-50 p-5">
          <div className="rounded-2xl bg-green-100 p-3">
            <GitBranch
              size={22}
              className="text-green-600"
            />
          </div>

          <div className="flex-1">
            <h4 className="font-semibold text-slate-900">
              Analyzing Pull Requests
            </h4>

            <p className="mt-1 text-sm text-slate-600">
              Detecting relationships between issues and
              pull requests.
            </p>
          </div>

          <Loader2
            size={18}
            className="animate-spin text-blue-600"
          />
        </div>

        <div className="flex items-center gap-4 rounded-2xl border border-slate-200 bg-slate-50 p-5">
          <div className="rounded-2xl bg-purple-100 p-3">
            <Brain
              size={22}
              className="text-purple-600"
            />
          </div>

          <div className="flex-1">
            <h4 className="font-semibold text-slate-900">
              Running AI Prediction Engine
            </h4>

            <p className="mt-1 text-sm text-slate-600">
              Computing confidence scores and contributor
              insights.
            </p>
          </div>

          <Loader2
            size={18}
            className="animate-spin text-blue-600"
          />
        </div>

        <div className="flex items-center gap-4 rounded-2xl border border-slate-200 bg-slate-50 p-5 opacity-70">
          <div className="rounded-2xl bg-emerald-100 p-3">
            <CheckCircle2
              size={22}
              className="text-emerald-600"
            />
          </div>

          <div className="flex-1">
            <h4 className="font-semibold text-slate-900">
              Preparing Dashboard
            </h4>

            <p className="mt-1 text-sm text-slate-600">
              Finalizing repository analytics and issue
              recommendations.
            </p>
          </div>
        </div>
      </div>

      {/* Footer */}

      <div className="border-t border-slate-100 px-8 py-6">
        <div className="rounded-2xl bg-blue-50 p-4 text-center">
          <p className="text-sm leading-6 text-slate-700">
            <span className="font-semibold">
              Tip:
            </span>{" "}
            Larger repositories may take a little longer to
            analyze because IssueScout evaluates issues,
            pull requests, repository activity, and
            contributor signals before generating results.
          </p>
        </div>
      </div>
    </div>
  );
}
