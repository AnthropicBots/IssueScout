import {
  Award,
  Brain,
  TrendingUp,
} from "lucide-react";

import {
  confidenceColor,
  formatConfidence,
} from "../../utils/formatters/formatConfidence";

interface PredictionScoreProps {
  confidence: number;
}

export default function PredictionScore({
  confidence,
}: PredictionScoreProps) {
  const colorMap = {
    green: {
      text: "text-emerald-600",
      badge:
        "bg-emerald-100 text-emerald-700",
      gradient:
        "from-emerald-500 to-green-600",
      label: "Excellent",
    },
    yellow: {
      text: "text-amber-600",
      badge:
        "bg-amber-100 text-amber-700",
      gradient:
        "from-amber-400 to-orange-500",
      label: "Medium",
    },
    red: {
      text: "text-red-600",
      badge:
        "bg-red-100 text-red-700",
      gradient:
        "from-red-500 to-rose-600",
      label: "Low",
    },
    blue: {
      text: "text-blue-600",
      badge:
        "bg-blue-100 text-blue-700",
      gradient:
        "from-blue-500 to-cyan-500",
      label: "High",
    },
  };

  const key = confidenceColor(confidence);

  const config =
    colorMap[key] ??
    {
      text: "text-blue-600",
      badge:
        "bg-blue-100 text-blue-700",
      gradient:
        "from-blue-500 to-cyan-500",
      label: "High",
    };

  return (
    <div className="overflow-hidden rounded-[2rem] border border-slate-200 bg-white shadow-sm transition-all duration-300 hover:shadow-xl">
      {/* Header */}

      <div className="border-b border-slate-100 p-6">
        <div className="flex items-center gap-3">
          <div className="rounded-2xl bg-blue-100 p-3">
            <Brain
              size={24}
              className="text-blue-600"
            />
          </div>

          <div>
            <h3 className="text-xl font-bold text-slate-900">
              Prediction Score
            </h3>

            <p className="mt-1 text-sm text-slate-500">
              AI confidence generated from repository analysis.
            </p>
          </div>
        </div>
      </div>

      {/* Score */}

      <div className="px-8 py-10 text-center">
        <p className="text-sm font-semibold uppercase tracking-[0.25em] text-slate-500">
          Prediction Confidence
        </p>

        <h2
          className={`mt-5 text-7xl font-black tracking-tight ${config.text}`}
        >
          {formatConfidence(confidence)}
        </h2>

        <div
          className={`mt-6 inline-flex items-center gap-2 rounded-full px-5 py-2 text-sm font-semibold ${config.badge}`}
        >
          <Award size={16} />
          {config.label}
        </div>

        {/* Progress */}

        <div className="mt-10">
          <div className="mb-3 flex items-center justify-between text-sm font-medium text-slate-500">
            <span>0%</span>

            <span>100%</span>
          </div>

          <div className="overflow-hidden rounded-full bg-slate-200">
            <div
              className={`h-4 rounded-full bg-gradient-to-r ${config.gradient} transition-all duration-700`}
              style={{
                width: `${confidence}%`,
              }}
            />
          </div>
        </div>

        {/* Footer */}

        <div className="mt-8 flex items-center justify-center gap-2 rounded-2xl bg-slate-50 p-4 text-slate-600">
          <TrendingUp
            size={18}
            className="text-blue-600"
          />

          <span className="text-sm font-medium">
            Confidence calculated using repository activity,
            issue metadata, pull request relationships, and
            contributor signals.
          </span>
        </div>
      </div>
    </div>
  );
}
