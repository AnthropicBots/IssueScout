interface PredictionInsightsProps {
  assigned: boolean;
  linkedPR: boolean;
}

export default function PredictionInsights({
  assigned,
  linkedPR,
}: PredictionInsightsProps) {
  return (
    <div className="rounded-xl border border-slate-200 bg-white p-5">

      <h3 className="mb-4 text-lg font-semibold">
        Prediction Insights
      </h3>

      <ul className="space-y-3 text-slate-600">

        <li>
          • Assignment Status:{" "}
          <strong>
            {assigned
              ? "Assigned"
              : "Unassigned"}
          </strong>
        </li>

        <li>
          • Linked Pull Request:{" "}
          <strong>
            {linkedPR
              ? "Available"
              : "Not Found"}
          </strong>
        </li>

        <li>
          • Confidence generated using
          repository activity and pull request
          relationships.
        </li>

      </ul>

    </div>
  );
}
