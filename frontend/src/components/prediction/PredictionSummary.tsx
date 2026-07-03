import PredictionInsights from "./PredictionInsights";
import PredictionRecommendation from "./PredictionRecommendation";
import PredictionScore from "./PredictionScore";

interface PredictionSummaryProps {
  confidence: number;
  assigned: boolean;
  linkedPR: boolean;
}

export default function PredictionSummary({
  confidence,
  assigned,
  linkedPR,
}: PredictionSummaryProps) {
  return (
    <div className="mt-2 grid gap-6 lg:grid-cols-3">

      <PredictionScore
        confidence={confidence}
      />

      <PredictionInsights
        assigned={assigned}
        linkedPR={linkedPR}
      />

      <PredictionRecommendation
        confidence={confidence}
      />

    </div>
  );
}
