import {
  CheckCircle2,
  Circle,
  ShieldCheck,
} from "lucide-react";

import type { CandidatePullRequestSummary } from "../../types/api";

interface PredictionEvidenceProps {
  candidates: CandidatePullRequestSummary[];
}

export default function PredictionEvidence({
  candidates,
}: PredictionEvidenceProps) {
  const topCandidate = candidates[0];

  const evidence = topCandidate?.evidence ?? [];

  const passed = evidence.filter((item) => item.passed).length;

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
            {topCandidate
              ? `Signals detected between this issue and pull request #${topCandidate.number}.`
              : "No candidate pull request has been analyzed for this issue."}
          </p>

        </div>

        {evidence.length > 0 && (
          <div className="rounded-full bg-blue-50 px-4 py-2 text-sm font-semibold text-blue-700">
            {passed}/{evidence.length}
          </div>
        )}

      </div>

      {evidence.length === 0 ? (

        <div className="rounded-2xl border border-dashed border-slate-300 px-4 py-10 text-center text-sm text-slate-500">
          No supporting evidence was found for this issue.
        </div>

      ) : (

        <div className="space-y-3">

          {evidence.map((item) => (

            <div
              key={item.type}
              className="flex items-center justify-between gap-4 rounded-2xl border border-slate-200 px-4 py-3"
            >

              <div className="min-w-0">
                <span className="font-medium text-slate-700">
                  {item.label}
                </span>

                <p className="mt-1 text-xs leading-5 text-slate-500">
                  {item.description}
                </p>
              </div>

              {item.passed ? (
                <CheckCircle2
                  size={20}
                  className="shrink-0 text-green-600"
                />
              ) : (
                <Circle
                  size={18}
                  className="shrink-0 text-slate-400"
                />
              )}

            </div>

          ))}

        </div>

      )}

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
