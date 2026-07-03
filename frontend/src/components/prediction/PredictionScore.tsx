import {
  confidenceColor,
  formatConfidence,
} from "../../utils/formatters/formatConfidence";
interface PredictionScoreProps {
  confidence: number;
}

export default function PredictionScore({
  confidence,
}: PredictionScoreProps) {
  const colorMap = {
    green: "text-green-600",
    yellow: "text-yellow-600",
    red: "text-red-600",
  };

  const color =
    colorMap[confidenceColor(confidence)];

  return (
    <div className="text-center">

      <p className="text-sm uppercase tracking-wide text-slate-500">
        Prediction Confidence
      </p>

      <h2 className={`mt-2 text-5xl font-bold ${color}`}>
        {formatConfidence(confidence)}
      </h2>

    </div>
  );
}
