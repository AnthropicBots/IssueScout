import {
  Activity,
  CheckCircle2,
  HeartPulse,
  TrendingUp,
} from "lucide-react";

interface RepositoryHealthChartProps {
  score: number;
}

export default function RepositoryHealthChart({
  score,
}: RepositoryHealthChartProps) {
  const health =
    score >= 90
      ? {
          label: "Excellent",
          icon: (
            <CheckCircle2
              size={18}
              className="text-emerald-600"
            />
          ),
          badge:
            "bg-emerald-100 text-emerald-700",
          progress:
            "from-emerald-500 to-green-500",
          description:
            "Repository is healthy and contributor friendly.",
        }
      : score >= 70
      ? {
          label: "Good",
          icon: (
            <TrendingUp
              size={18}
              className="text-blue-600"
            />
          ),
          badge:
            "bg-blue-100 text-blue-700",
          progress:
            "from-blue-500 to-cyan-500",
          description:
            "Repository shows healthy contribution activity.",
        }
      : score >= 50
      ? {
          label: "Needs Review",
          icon: (
            <Activity
              size={18}
              className="text-amber-600"
            />
          ),
          badge:
            "bg-amber-100 text-amber-700",
          progress:
            "from-amber-500 to-orange-500",
          description:
            "Repository is active but requires additional review.",
        }
      : {
          label: "Low",
          icon: (
            <HeartPulse
              size={18}
              className="text-red-600"
            />
          ),
          badge:
            "bg-red-100 text-red-700",
          progress:
            "from-red-500 to-rose-500",
          description:
            "Repository requires manual inspection before contribution.",
        };

  return (
    <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">

      {/* Header */}

      <div className="flex items-center gap-3">

        <div className="rounded-2xl bg-blue-100 p-3">

          <HeartPulse
            size={20}
            className="text-blue-600"
          />

        </div>

        <div>

          <h3 className="font-bold text-slate-900">
            Repository Health
          </h3>

          <p className="text-sm text-slate-500">
            Overall repository quality
          </p>

        </div>

      </div>

      {/* Score */}

      <div className="mt-8 text-center">

        <div className="text-6xl font-black text-slate-900">

          {score}%

        </div>

        <div
          className={`mt-4 inline-flex items-center gap-2 rounded-full px-4 py-2 text-sm font-semibold ${health.badge}`}
        >

          {health.icon}

          {health.label}

        </div>

      </div>

      {/* Progress */}

      <div className="mt-8">

        <div className="mb-2 flex justify-between text-sm text-slate-500">

          <span>Health Score</span>

          <span>{score}%</span>

        </div>

        <div className="h-3 overflow-hidden rounded-full bg-slate-200">

          <div
            className={`h-full rounded-full bg-gradient-to-r ${health.progress} transition-all duration-700`}
            style={{
              width: `${score}%`,
            }}
          />

        </div>

      </div>

      {/* Summary */}

      <div className="mt-8 rounded-2xl bg-slate-50 p-4">

        <p className="font-semibold text-slate-900">

          {health.label}

        </p>

        <p className="mt-2 text-sm leading-6 text-slate-600">

          {health.description}

        </p>

      </div>

      {/* Quick Metrics */}

      <div className="mt-6 grid grid-cols-3 gap-3">

        <div className="rounded-xl bg-slate-50 p-3 text-center">

          <div className="text-xs uppercase tracking-wide text-slate-500">
            Stability
          </div>

          <div className="mt-1 font-bold text-slate-900">
            High
          </div>

        </div>

        <div className="rounded-xl bg-slate-50 p-3 text-center">

          <div className="text-xs uppercase tracking-wide text-slate-500">
            Activity
          </div>

          <div className="mt-1 font-bold text-slate-900">
            Active
          </div>

        </div>

        <div className="rounded-xl bg-slate-50 p-3 text-center">

          <div className="text-xs uppercase tracking-wide text-slate-500">
            AI Status
          </div>

          <div className="mt-1 font-bold text-slate-900">
            Ready
          </div>

        </div>

      </div>

    </div>
  );
}
