import {
  Brain,
  Sparkles,
} from "lucide-react";

import PredictionEvidence from "./PredictionEvidence";
import PredictionInsights from "./PredictionInsights";
import PredictionRecommendation from "./PredictionRecommendation";
import PredictionScore from "./PredictionScore";

interface PredictionSummaryProps {
  confidence: number;
  assigned: boolean;
  linkedPR: boolean;
}

export default function PredictionSummary({
  confidence,
  assigned,
  linkedPR,
}: PredictionSummaryProps) {
  return (
    <section className="mt-4 space-y-8">
      {/* Header */}

      <div className="overflow-hidden rounded-[2rem] border border-slate-200 bg-gradient-to-br from-slate-950 via-slate-900 to-blue-950 text-white shadow-[0_25px_60px_rgba(15,23,42,0.20)]">
        <div className="flex flex-col gap-8 p-8 lg:flex-row lg:items-center lg:justify-between lg:p-10">
          <div>
            <div className="inline-flex items-center gap-2 rounded-full border border-cyan-400/30 bg-white/10 px-4 py-2 text-sm font-semibold text-cyan-200 backdrop-blur">
              <Brain size={16} />

              AI Prediction Engine
            </div>

            <h2 className="mt-5 text-4xl font-black tracking-tight">
              Prediction Analysis
            </h2>

            <p className="mt-4 max-w-3xl text-lg leading-8 text-slate-300">
              IssueScout evaluates repository activity,
              issue metadata, contributor information,
              and pull request relationships to generate
              intelligent confidence scores and
              actionable recommendations.
            </p>
          </div>

          <div className="rounded-3xl border border-white/10 bg-white/10 px-8 py-6 text-center backdrop-blur">
            <p className="text-sm uppercase tracking-[0.2em] text-slate-300">
              AI Confidence
            </p>

            <h3 className="mt-2 text-5xl font-black text-cyan-300">
              {confidence}%
            </h3>

            <div className="mt-4 inline-flex items-center gap-2 rounded-full bg-cyan-400/20 px-4 py-2 text-sm font-semibold text-cyan-200">
              <Sparkles size={16} />
              Repository Intelligence
            </div>
          </div>
        </div>
      </div>

      {/* Analysis Cards */}

      <div className="grid gap-6 xl:grid-cols-2">
        <PredictionScore
          confidence={confidence}
        />

        <PredictionRecommendation
          confidence={confidence}
        />

        <PredictionInsights
          assigned={assigned}
          linkedPR={linkedPR}
        />

        <PredictionEvidence
          confidence={confidence}
          assigned={assigned}
          linkedPR={linkedPR}
        />
      </div>
    </section>
  );
}
