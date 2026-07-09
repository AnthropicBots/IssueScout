import {
  CheckCircle2,
  GitPullRequest,
  Lightbulb,
  User,
} from "lucide-react";

interface PredictionInsightsProps {
  assigned: boolean;
  linkedPR: boolean;
}

export default function PredictionInsights({
  assigned,
  linkedPR,
}: PredictionInsightsProps) {
  const insights = [
    {
      icon: <User size={20} />,
      title: "Assignment Status",
      value: assigned
        ? "Assigned"
        : "Unassigned",
      color: assigned
        ? "bg-green-100 text-green-600"
        : "bg-orange-100 text-orange-600",
      description: assigned
        ? "A contributor is currently assigned to this issue."
        : "No contributor is currently assigned.",
    },
    {
      icon: <GitPullRequest size={20} />,
      title: "Linked Pull Request",
      value: linkedPR
        ? "Available"
        : "Not Found",
      color: linkedPR
        ? "bg-blue-100 text-blue-600"
        : "bg-slate-100 text-slate-600",
      description: linkedPR
        ? "IssueScout identified a related pull request."
        : "No related pull request could be confidently detected.",
    },
    {
      icon: <CheckCircle2 size={20} />,
      title: "Prediction Engine",
      value: "AI Analysis",
      color:
        "bg-purple-100 text-purple-600",
      description:
        "Confidence is calculated using repository activity, issue metadata, pull request relationships, and contributor signals.",
    },
  ];

  return (
    <div className="rounded-[1.75rem] border border-slate-200 bg-white shadow-sm transition-all duration-300 hover:shadow-lg">
      {/* Header */}

      <div className="border-b border-slate-100 p-6">
        <div className="flex items-center gap-3">
          <div className="rounded-2xl bg-blue-100 p-3">
            <Lightbulb
              size={22}
              className="text-blue-600"
            />
          </div>

          <div>
            <h3 className="text-xl font-bold text-slate-900">
              Prediction Insights
            </h3>

            <p className="mt-1 text-sm text-slate-500">
              AI-generated insights from repository analysis.
            </p>
          </div>
        </div>
      </div>

      {/* Insights */}

      <div className="space-y-4 p-6">
        {insights.map((item) => (
          <div
            key={item.title}
            className="flex gap-4 rounded-2xl border border-slate-200 bg-slate-50 p-5 transition-all duration-200 hover:border-blue-200 hover:bg-white"
          >
            <div
              className={`flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl ${item.color}`}
            >
              {item.icon}
            </div>

            <div className="min-w-0 flex-1">
              <div className="flex flex-col gap-1 sm:flex-row sm:items-center sm:justify-between">
                <h4 className="font-semibold text-slate-900">
                  {item.title}
                </h4>

                <span className="rounded-full bg-white px-3 py-1 text-sm font-semibold text-slate-700 shadow-sm">
                  {item.value}
                </span>
              </div>

              <p className="mt-3 text-sm leading-6 text-slate-600">
                {item.description}
              </p>
            </div>
          </div>
        ))}
      </div>

      {/* Footer */}

      <div className="border-t border-slate-100 px-6 py-5">
        <div className="rounded-2xl bg-gradient-to-r from-blue-50 to-cyan-50 p-4">
          <p className="text-sm leading-6 text-slate-700">
            <span className="font-semibold">
              IssueScout Insight:
            </span>{" "}
            Prediction quality improves by combining issue
            metadata, pull request relationships, repository
            activity, and contributor information rather than
            relying on a single signal.
          </p>
        </div>
      </div>
    </div>
  );
}
