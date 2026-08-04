import type { ReactNode } from "react";

import {
  AlertTriangle,
  CheckCircle2,
  ShieldCheck,
  Star,
} from "lucide-react";

import {
  getConfidenceTier,
  type ConfidenceTierKey,
} from "../../utils/formatters/formatConfidence";

interface PredictionRecommendationProps {
  confidence: number;
}

interface RecommendationCopy {
  title: string;
  description: string;
  icon: ReactNode;
  badge: string;
}

const RECOMMENDATION_COPY: Record<ConfidenceTierKey, RecommendationCopy> = {
  excellent: {
    title: "Highly Recommended",
    description:
      "This issue is an excellent candidate for contribution. The prediction confidence is extremely high and the detected repository signals strongly support the analysis.",
    icon: (
      <Star
        size={24}
        className="text-emerald-600"
      />
    ),
    badge: "Excellent Match",
  },
  high: {
    title: "Recommended",
    description:
      "This issue appears suitable for contribution. Review the issue details and linked pull requests before starting your implementation.",
    icon: (
      <CheckCircle2
        size={24}
        className="text-blue-600"
      />
    ),
    badge: "Good Match",
  },
  medium: {
    title: "Review Recommended",
    description:
      "The prediction contains moderate confidence. Verify the issue discussion and repository activity before contributing.",
    icon: (
      <ShieldCheck
        size={24}
        className="text-amber-600"
      />
    ),
    badge: "Needs Review",
  },
  low: {
    title: "Manual Verification Required",
    description:
      "Prediction confidence is low. Carefully inspect the issue, related discussions, and repository history before proceeding.",
    icon: (
      <AlertTriangle
        size={24}
        className="text-red-600"
      />
    ),
    badge: "Low Confidence",
  },
};

export default function PredictionRecommendation({
  confidence,
}: PredictionRecommendationProps) {
  const tier = getConfidenceTier(confidence);
  const copy = RECOMMENDATION_COPY[tier.key];

  return (
    <div
      className={`overflow-hidden rounded-[1.75rem] border ${tier.borderClass} bg-gradient-to-br ${tier.backgroundClass} shadow-sm transition-all duration-300 hover:shadow-lg`}
    >
      {/* Header */}

      <div className="flex items-center justify-between border-b border-white/60 p-6">
        <div className="flex items-center gap-4">
          <div className="rounded-2xl bg-white p-3 shadow-sm">
            {copy.icon}
          </div>

          <div>
            <h3 className="text-xl font-bold text-slate-900">
              Recommendation
            </h3>

            <p className="mt-1 text-sm text-slate-600">
              AI-generated contribution guidance
            </p>
          </div>
        </div>

        <span
          className={`rounded-full px-4 py-2 text-sm font-semibold ${tier.badgeClass}`}
        >
          {copy.badge}
        </span>
      </div>

      {/* Content */}

      <div className="space-y-5 p-6">
        <h4 className="text-2xl font-black tracking-tight text-slate-900">
          {copy.title}
        </h4>

        <p className="leading-8 text-slate-700">
          {copy.description}
        </p>

        <div className="rounded-2xl border border-white/70 bg-white/70 p-5 backdrop-blur">
          <p className="text-sm font-semibold uppercase tracking-wide text-slate-500">
            Confidence Score
          </p>

          <div className="mt-3 flex items-center justify-between">
            <span className="text-4xl font-black text-slate-900">
              {confidence}%
            </span>

            <span
              className={`rounded-full px-4 py-2 text-sm font-semibold ${tier.badgeClass}`}
            >
              {copy.badge}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}
