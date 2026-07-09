import {
  CheckCircle2,
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
      passed: linkedPR,
    },
    {
      label: "Issue Assigned",
      passed: assigned,
    },
    {
      label: "High Confidence Prediction",
      passed: confidence >= 80,
    },
  ];

  return (
    <div className="rounded-xl border border-slate-200 bg-white p-6">
      <h3 className="mb-4 text-lg font-semibold">
        Prediction Evidence
      </h3>

      <div className="space-y-3">
        {evidence.map((item) => (
          <div
            key={item.label}
            className="flex items-center justify-between"
          >
            <span>{item.label}</span>

            {item.passed ? (
              <CheckCircle2
                className="text-green-600"
                size={20}
              />
            ) : (
              <XCircle
                className="text-red-500"
                size={20}
              />
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
