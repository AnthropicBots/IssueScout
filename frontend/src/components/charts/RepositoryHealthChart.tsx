interface RepositoryHealthChartProps {
  score: number;
}

export default function RepositoryHealthChart({
  score,
}: RepositoryHealthChartProps) {
  const level =
    score >= 80
      ? "Excellent"
      : score >= 60
      ? "Good"
      : "Needs Review";

  return (
    <div className="rounded-xl border border-slate-200 bg-white p-6">

      <h3 className="font-semibold">
        Repository Health
      </h3>

      <div className="mt-6">

        <div className="h-4 overflow-hidden rounded-full bg-slate-200">

          <div
            className="h-full rounded-full bg-gradient-to-r from-blue-500 to-green-500"
            style={{
              width: `${score}%`,
            }}
          />

        </div>

        <div className="mt-4 flex items-center justify-between">

          <span className="font-semibold">
            {score}%
          </span>

          <span className="text-slate-500">
            {level}
          </span>

        </div>

      </div>

    </div>
  );
}
