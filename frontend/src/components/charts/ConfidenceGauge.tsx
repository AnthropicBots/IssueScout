import {
  Brain,
  Sparkles,
} from "lucide-react";

interface ConfidenceGaugeProps {
  value: number;
}

export default function ConfidenceGauge({
  value,
}: ConfidenceGaugeProps) {

  const level =
    value >= 90
      ? {
          label: "Excellent",
          color: "text-emerald-600",
          badge:
            "bg-emerald-100 text-emerald-700",
          progress:
            "from-emerald-500 to-green-500",
        }
      : value >= 70
      ? {
          label: "High",
          color: "text-blue-600",
          badge:
            "bg-blue-100 text-blue-700",
          progress:
            "from-blue-500 to-cyan-500",
        }
      : value >= 50
      ? {
          label: "Medium",
          color: "text-amber-600",
          badge:
            "bg-amber-100 text-amber-700",
          progress:
            "from-amber-500 to-orange-500",
        }
      : {
          label: "Low",
          color: "text-red-600",
          badge:
            "bg-red-100 text-red-700",
          progress:
            "from-red-500 to-rose-500",
        };

  return (

    <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">

      {/* Header */}

      <div className="flex items-center justify-between">

        <div className="flex items-center gap-3">

          <div className="rounded-2xl bg-blue-100 p-3">

            <Brain
              size={20}
              className="text-blue-600"
            />

          </div>

          <div>

            <h3 className="font-bold text-slate-900">
              Confidence
            </h3>

            <p className="text-sm text-slate-500">
              AI Prediction Score
            </p>

          </div>

        </div>

        <div
          className={`rounded-full px-3 py-1 text-xs font-semibold ${level.badge}`}
        >
          {level.label}
        </div>

      </div>

      {/* Score */}

      <div className="mt-8 text-center">

        <div
          className={`text-6xl font-black ${level.color}`}
        >
          {value}%
        </div>

        <p className="mt-2 text-slate-500">
          Repository Confidence
        </p>

      </div>

      {/* Progress */}

      <div className="mt-8">

        <div className="mb-2 flex justify-between text-sm text-slate-500">

          <span>0%</span>

          <span>100%</span>

        </div>

        <div className="h-3 overflow-hidden rounded-full bg-slate-200">

          <div
            className={`h-full rounded-full bg-gradient-to-r ${level.progress} transition-all duration-700`}
            style={{
              width: `${value}%`,
            }}
          />

        </div>

      </div>

      {/* Footer */}

      <div className="mt-8 rounded-2xl bg-slate-50 p-4">

        <div className="flex items-center gap-2">

          <Sparkles
            size={18}
            className="text-blue-600"
          />

          <span className="font-semibold text-slate-700">
            AI Repository Intelligence
          </span>

        </div>

        <p className="mt-2 text-sm leading-6 text-slate-600">

          Confidence combines repository activity,
          issue metadata, pull request relationships,
          contributor information and historical
          repository signals.

        </p>

      </div>

    </div>

  );

}
