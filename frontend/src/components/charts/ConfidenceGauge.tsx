interface ConfidenceGaugeProps {
  value: number;
}

export default function ConfidenceGauge({
  value,
}: ConfidenceGaugeProps) {
  const {
    textColor,
    strokeColor,
    badgeColor,
    label,
  } =
    value >= 90
      ? {
          textColor: "text-emerald-600",
          strokeColor: "#10b981",
          badgeColor:
            "bg-emerald-100 text-emerald-700",
          label: "Excellent",
        }
      : value >= 70
      ? {
          textColor: "text-blue-600",
          strokeColor: "#2563eb",
          badgeColor:
            "bg-blue-100 text-blue-700",
          label: "High",
        }
      : value >= 50
      ? {
          textColor: "text-amber-600",
          strokeColor:
            "#f59e0b",
          badgeColor:
            "bg-amber-100 text-amber-700",
          label: "Medium",
        }
      : {
          textColor: "text-red-600",
          strokeColor: "#ef4444",
          badgeColor:
            "bg-red-100 text-red-700",
          label: "Low",
        };

  const radius = 56;
  const circumference =
    2 * Math.PI * radius;

  const progress =
    circumference -
    (value / 100) * circumference;

  return (
    <div className="flex flex-col items-center">
      <div className="mb-6 text-center">
        <h3 className="text-xl font-bold text-slate-900">
          Confidence Score
        </h3>

        <p className="mt-2 text-sm text-slate-500">
          Average AI prediction confidence
        </p>
      </div>

      <div className="relative">
        <svg
          width="160"
          height="160"
          className="-rotate-90"
        >
          <circle
            cx="80"
            cy="80"
            r={radius}
            fill="none"
            stroke="#e2e8f0"
            strokeWidth="12"
          />

          <circle
            cx="80"
            cy="80"
            r={radius}
            fill="none"
            stroke={strokeColor}
            strokeWidth="12"
            strokeLinecap="round"
            strokeDasharray={
              circumference
            }
            strokeDashoffset={
              progress
            }
            style={{
              transition:
                "stroke-dashoffset 700ms ease",
            }}
          />
        </svg>

        <div className="absolute inset-0 flex flex-col items-center justify-center">
          <h2
            className={`text-4xl font-black ${textColor}`}
          >
            {value}%
          </h2>

          <p className="mt-1 text-sm font-medium text-slate-500">
            Confidence
          </p>
        </div>
      </div>

      <div
        className={`mt-8 rounded-full px-5 py-2 text-sm font-semibold ${badgeColor}`}
      >
        {label}
      </div>
    </div>
  );
}
