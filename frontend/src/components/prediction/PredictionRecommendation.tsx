interface PredictionRecommendationProps {
  confidence: number;
}

export default function PredictionRecommendation({
  confidence,
}: PredictionRecommendationProps) {
  const recommendation =
    confidence >= 80
      ? "Highly recommended for contributors."
      : confidence >= 60
      ? "Worth reviewing before contributing."
      : "Requires manual verification.";

  return (
    <div className="rounded-xl border border-blue-200 bg-blue-50 p-5">

      <h3 className="font-semibold text-blue-800">
        Recommendation
      </h3>

      <p className="mt-2 text-blue-700">
        {recommendation}
      </p>

    </div>
  );
}
