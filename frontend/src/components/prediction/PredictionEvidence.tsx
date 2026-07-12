import {
  CheckCircle2,
  Circle,
  ShieldCheck,
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
      passed: linkedPR,
    },
    {
      label: "Assigned Contributor",
      passed: assigned,
    },
    {
      label: "High Confidence (>80%)",
      passed: confidence >= 80,
    },
    {
      label: "Repository Successfully Analyzed",
      passed: true,
    },
    {
      label: "Prediction Generated",
      passed: true,
    },
  ];

  const passed = evidence.filter((e) => e.passed).length;

  return (
    <div className="rounded-3xl border border-slate-200 bg-white p-6">

      <div className="mb-6 flex items-center justify-between">

        <div>

          <div className="flex items-center gap-2">

            <ShieldCheck
              size={20}
              className="text-blue-600"
            />

            <h3 className="text-xl font-bold text-slate-900">
              Evidence Analysis
            </h3>

          </div>

          <p className="mt-2 text-sm text-slate-500">
            Signals used by IssueScout to generate the prediction.
          </p>

        </div>

        <div className="rounded-full bg-blue-50 px-4 py-2 text-sm font-semibold text-blue-700">
          {passed}/{evidence.length}
        </div>

      </div>

      <div className="space-y-3">

        {evidence.map((item) => (

          <div
            key={item.label}
            className="flex items-center justify-between rounded-2xl border border-slate-200 px-4 py-3"
          >

            <span className="font-medium text-slate-700">
              {item.label}
            </span>

            {item.passed ? (
              <CheckCircle2
                size={20}
                className="text-green-600"
              />
            ) : (
              <Circle
                size={18}
                className="text-slate-400"
              />
            )}

          </div>

        ))}

      </div>

      <div className="mt-6 rounded-2xl bg-slate-50 p-4">

        <p className="text-sm leading-6 text-slate-600">

          The confidence score is calculated from repository
          activity, issue metadata, relationship detection,
          contributor information and pull request evidence.

        </p>

      </div>

    </div>
  );
}
