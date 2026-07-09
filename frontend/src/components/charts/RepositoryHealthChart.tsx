import {
  Activity,
  CheckCircle2,
  TrendingUp,
} from "lucide-react";

interface RepositoryHealthChartProps {
  score: number;
}

export default function RepositoryHealthChart({
  score,
}: RepositoryHealthChartProps) {
  const {
    level,
    progressColor,
    badgeColor,
    icon,
  } =
    score >= 90
      ? {
          level: "Excellent",
          progressColor:
            "from-emerald-500 to-green-600",
          badgeColor:
            "bg-emerald-100 text-emerald-700",
          icon: (
            <CheckCircle2
              size={20}
              className="text-emerald-600"
            />
          ),
        }
      : score >= 70
      ? {
          level: "Good",
          progressColor:
            "from-blue-500 to-cyan-500",
          badgeColor:
            "bg-blue-100 text-blue-700",
          icon: (
            <TrendingUp
              size={20}
              className="text-blue-600"
            />
          ),
        }
      : {
          level: "Needs Review",
          progressColor:
            "from-amber-500 to-orange-500",
          badgeColor:
            "bg-amber-100 text-amber-700",
          icon: (
            <Activity
              size={20}
              className="text-amber-600"
            />
          ),
        };

  return (
    <div className="rounded-[1.75rem] border border-slate-200 bg-white p-6 shadow-sm transition-all duration-300 hover:shadow-lg">
      {/* Header */}

      <div className="mb-6">
        <h3 className="text-xl font-bold text-slate-900">
          Repository Health
        </h3>

        <p className="mt-2 text-sm text-slate-500">
          Overall health based on IssueScout's repository
          analysis.
        </p>
      </div>

      {/* Score */}

      <div className="mb-8 text-center">
        <div className="text-5xl font-black tracking-tight text-slate-900">
          {score}%
        </div>

        <div
          className={`mt-4 inline-flex items-center gap-2 rounded-full px-4 py-2 text-sm font-semibold ${badgeColor}`}
        >
          {icon}
          {level}
        </div>
      </div>

      {/* Progress */}

      <div>
        <div className="mb-3 flex items-center justify-between text-sm font-medium text-slate-500">
          <span>Health Score</span>

          <span>{score}%</span>
        </div>

        <div className="overflow-hidden rounded-full bg-slate-200">
          <div
            className={`h-4 rounded-full bg-gradient-to-r ${progressColor} transition-all duration-700`}
            style={{
              width: `${score}%`,
            }}
          />
        </div>
      </div>

      {/* Legend */}

      <div className="mt-8 grid grid-cols-3 gap-3 text-center">
        <div className="rounded-xl bg-red-50 p-3">
          <div className="text-xs font-semibold uppercase tracking-wide text-red-600">
            Low
          </div>

          <div className="mt-1 text-sm text-slate-600">
            0–69%
          </div>
        </div>

        <div className="rounded-xl bg-blue-50 p-3">
          <div className="text-xs font-semibold uppercase tracking-wide text-blue-600">
            Good
          </div>

          <div className="mt-1 text-sm text-slate-600">
            70–89%
          </div>
        </div>

        <div className="rounded-xl bg-green-50 p-3">
          <div className="text-xs font-semibold uppercase tracking-wide text-green-600">
            Excellent
          </div>

          <div className="mt-1 text-sm text-slate-600">
            90–100%
          </div>
        </div>
      </div>
    </div>
  );
}
