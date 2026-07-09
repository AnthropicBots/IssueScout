import PredictionInsights from "./PredictionInsights";
import PredictionRecommendation from "./PredictionRecommendation";
import PredictionScore from "./PredictionScore";
import PredictionEvidence from "./PredictionEvidence";

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
    <div className="mt-2 grid gap-6 xl:grid-cols-4">

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

      <PredictionEvidence
        confidence={confidence}
        assigned={assigned}
        linkedPR={linkedPR}
      />

    </div>
  );
}
