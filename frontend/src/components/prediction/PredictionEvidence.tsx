import {
  CheckCircle2,
  ShieldCheck,
  Sparkles,
  XCircle,
} from "lucide-react";

interface PredictionEvidenceProps {
  linkedPR: boolean;
  assigned: boolean;
  confidence: number;
}

export default function PredictionEvidence({
  linkedPR,
  assigned,
  confidence,
}: PredictionEvidenceProps) {
  const evidence = [
    {
      label: "Linked Pull Request",
      description:
        "A pull request has been associated with this issue.",
      passed: linkedPR,
    },
    {
      label: "Issue Assigned",
      description:
        "The issue currently has an assigned contributor.",
      passed: assigned,
    },
    {
      label: "High Confidence Prediction",
      description:
        "Prediction confidence is at least 80%.",
      passed: confidence >= 80,
    },
  ];

  const passedCount = evidence.filter(
    (item) => item.passed,
  ).length;

  return (
    <div className="rounded-[1.75rem] border border-slate-200 bg-white shadow-sm transition-all duration-300 hover:shadow-lg">
      {/* Header */}

      <div className="border-b border-slate-100 p-6">
        <div className="flex items-center justify-between">
          <div>
            <div className="mb-2 flex items-center gap-2">
              <ShieldCheck
                size={20}
                className="text-blue-600"
              />

              <h3 className="text-xl font-bold text-slate-900">
                Prediction Evidence
              </h3>
            </div>

            <p className="text-sm text-slate-500">
              Signals used by IssueScout to evaluate this
              prediction.
            </p>
          </div>

          <div className="rounded-full bg-blue-50 px-4 py-2 text-sm font-semibold text-blue-700">
            {passedCount}/{evidence.length} Passed
          </div>
        </div>
      </div>

      {/* Evidence */}

      <div className="space-y-4 p-6">
        {evidence.map((item) => (
          <div
            key={item.label}
            className={`flex items-start justify-between rounded-2xl border p-5 transition-all ${
              item.passed
                ? "border-green-200 bg-green-50"
                : "border-red-200 bg-red-50"
            }`}
          >
            <div className="pr-4">
              <h4 className="font-semibold text-slate-900">
                {item.label}
              </h4>

              <p className="mt-2 text-sm leading-6 text-slate-600">
                {item.description}
              </p>
            </div>

            {item.passed ? (
              <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-green-100">
                <CheckCircle2
                  size={22}
                  className="text-green-600"
                />
              </div>
            ) : (
              <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-red-100">
                <XCircle
                  size={22}
                  className="text-red-600"
                />
              </div>
            )}
          </div>
        ))}
      </div>

      {/* Footer */}

      <div className="border-t border-slate-100 px-6 py-5">
        <div className="inline-flex items-center gap-2 rounded-full bg-slate-100 px-4 py-2 text-sm font-medium text-slate-700">
          <Sparkles
            size={16}
            className="text-blue-600"
          />
          Evidence collected during repository analysis
        </div>
      </div>
    </div>
  );
}
