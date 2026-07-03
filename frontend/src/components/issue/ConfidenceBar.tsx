interface ConfidenceBarProps {
  value: number;
}

export default function ConfidenceBar({
  value,
}: ConfidenceBarProps) {
  const color =
    value >= 90
      ? "bg-green-500"
      : value >= 70
      ? "bg-blue-500"
      : value >= 50
      ? "bg-yellow-500"
      : "bg-red-500";

  return (
    <div className="space-y-2">
      <div className="flex items-center justify-between text-sm">
        <span className="font-medium text-slate-600">
          Confidence
        </span>

        <span className="font-semibold text-slate-900">
          {value}%
        </span>
      </div>

      <div className="h-2 overflow-hidden rounded-full bg-slate-200">
        <div
          className={`h-full rounded-full transition-all duration-700 ${color}`}
          style={{ width: `${value}%` }}
        />
      </div>
    </div>
  );
}
