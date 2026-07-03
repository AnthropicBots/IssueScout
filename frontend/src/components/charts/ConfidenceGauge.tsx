interface ConfidenceGaugeProps {
  value: number;
}

export default function ConfidenceGauge({
  value,
}: ConfidenceGaugeProps) {
  const color =
    value >= 80
      ? "text-green-600"
      : value >= 50
      ? "text-yellow-600"
      : "text-red-600";

  const stroke =
    value >= 80
      ? "stroke-green-500"
      : value >= 50
      ? "stroke-yellow-500"
      : "stroke-red-500";

  const radius = 52;
  const circumference = 2 * Math.PI * radius;
  const progress =
    circumference - (value / 100) * circumference;

  return (
    <div className="flex flex-col items-center">

      <svg
        width="140"
        height="140"
        className="-rotate-90"
      >
        <circle
          cx="70"
          cy="70"
          r={radius}
          fill="none"
          strokeWidth="10"
          className="stroke-slate-200"
        />

        <circle
          cx="70"
          cy="70"
          r={radius}
          fill="none"
          strokeWidth="10"
          strokeLinecap="round"
          strokeDasharray={circumference}
          strokeDashoffset={progress}
          className={stroke}
        />
      </svg>

      <div className="-mt-24 text-center">

        <h2 className={`text-4xl font-bold ${color}`}>
          {value}%
        </h2>

        <p className="mt-2 text-sm text-slate-500">
          Confidence
        </p>

      </div>

    </div>
  );
}
