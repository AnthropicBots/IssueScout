interface ConfidenceBarProps {
  value: number;
}

export default function ConfidenceBar({
  value,
}: ConfidenceBarProps) {
  const {
    barColor,
    badgeColor,
    label,
  } =
    value >= 90
      ? {
          barColor:
            "bg-gradient-to-r from-emerald-500 to-green-600",
          badgeColor:
            "bg-emerald-100 text-emerald-700",
          label: "Excellent",
        }
      : value >= 70
      ? {
          barColor:
            "bg-gradient-to-r from-blue-500 to-cyan-500",
          badgeColor:
            "bg-blue-100 text-blue-700",
          label: "High",
        }
      : value >= 50
      ? {
          barColor:
            "bg-gradient-to-r from-amber-400 to-yellow-500",
          badgeColor:
            "bg-yellow-100 text-yellow-700",
          label: "Medium",
        }
      : {
          barColor:
            "bg-gradient-to-r from-red-500 to-rose-600",
          badgeColor:
            "bg-red-100 text-red-700",
          label: "Low",
        };

  return (
    <div className="space-y-4">
      {/* Header */}

      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm font-semibold uppercase tracking-wide text-slate-500">
            Prediction Confidence
          </p>

          <p className="mt-1 text-2xl font-black tracking-tight text-slate-900">
            {value}%
          </p>
        </div>

        <span
          className={`rounded-full px-4 py-2 text-sm font-semibold ${badgeColor}`}
        >
          {label}
        </span>
      </div>

      {/* Progress */}

      <div className="relative h-4 overflow-hidden rounded-full bg-slate-200">
        <div
          className={`h-full rounded-full transition-all duration-700 ease-out ${barColor}`}
          style={{
            width: `${value}%`,
          }}
        />
      </div>

      {/* Footer */}

      <div className="flex items-center justify-between text-sm text-slate-500">
        <span>0%</span>

        <span className="font-medium">
          AI Confidence Score
        </span>

        <span>100%</span>
      </div>
    </div>
  );
}
