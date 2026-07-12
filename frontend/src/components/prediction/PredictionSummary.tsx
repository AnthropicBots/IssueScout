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
    <section className="space-y-6">

      {/* Compact Header */}

      <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">

        <div className="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between">

          <div>

            <div className="inline-flex items-center gap-2 rounded-full bg-blue-50 px-4 py-2 text-sm font-semibold text-blue-700">

              <Brain size={16} />

              AI Prediction Engine

            </div>

            <h2 className="mt-4 text-3xl font-black text-slate-900">
              Prediction Analysis
            </h2>

            <p className="mt-3 max-w-2xl text-slate-600">
              Repository intelligence generated from issue
              metadata, pull request relationships,
              contributor activity and repository signals.
            </p>

          </div>

          <div className="rounded-3xl bg-gradient-to-br from-blue-600 to-cyan-500 px-8 py-6 text-center text-white shadow-lg">

            <div className="text-sm uppercase tracking-widest opacity-80">
              Confidence
            </div>

            <div className="mt-2 text-5xl font-black">
              {confidence}%
            </div>

            <div className="mt-4 inline-flex items-center gap-2 rounded-full bg-white/20 px-4 py-2 text-sm">

              <Sparkles size={15} />

              AI Prediction

            </div>

          </div>

        </div>

      </div>

      {/* Dashboard */}

      <div className="grid gap-5 xl:grid-cols-2">

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
