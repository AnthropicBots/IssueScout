export type ConfidenceTierKey =
  | "excellent"
  | "high"
  | "medium"
  | "low";

export type BadgeColorName =
  | "green"
  | "blue"
  | "yellow"
  | "red";

export interface ConfidenceTier {
  key: ConfidenceTierKey;
  label: string;
  badgeColor: BadgeColorName;
  textClass: string;
  badgeClass: string;
  gradientClass: string;
  backgroundClass: string;
  borderClass: string;
}

/**
 * Single source of truth for "what does this confidence number mean".
 * Every component that needs a confidence-driven color, label, or
 * gradient should read it from here instead of re-deriving its own
 * thresholds - previously PredictionRecommendation, PredictionScore,
 * PredictionEvidence and this file each had their own, disagreeing
 * boundaries (80/50 in one place, 90/70/50 in another).
 *
 * Boundaries follow the more granular 90/70/50 scheme (previously only
 * used by PredictionRecommendation) since it distinguishes "high" from
 * "excellent", which the flatter 80/50 scheme collapsed together.
 */
const CONFIDENCE_TIERS: Record<ConfidenceTierKey, ConfidenceTier> = {
  excellent: {
    key: "excellent",
    label: "Excellent",
    badgeColor: "green",
    textClass: "text-emerald-600",
    badgeClass: "bg-emerald-100 text-emerald-700",
    gradientClass: "from-emerald-500 to-green-600",
    backgroundClass: "from-emerald-50 to-green-50",
    borderClass: "border-emerald-200",
  },
  high: {
    key: "high",
    label: "High",
    badgeColor: "blue",
    textClass: "text-blue-600",
    badgeClass: "bg-blue-100 text-blue-700",
    gradientClass: "from-blue-500 to-cyan-500",
    backgroundClass: "from-blue-50 to-cyan-50",
    borderClass: "border-blue-200",
  },
  medium: {
    key: "medium",
    label: "Medium",
    badgeColor: "yellow",
    textClass: "text-amber-600",
    badgeClass: "bg-amber-100 text-amber-700",
    gradientClass: "from-amber-400 to-orange-500",
    backgroundClass: "from-amber-50 to-yellow-50",
    borderClass: "border-amber-200",
  },
  low: {
    key: "low",
    label: "Low",
    badgeColor: "red",
    textClass: "text-red-600",
    badgeClass: "bg-red-100 text-red-700",
    gradientClass: "from-red-500 to-rose-600",
    backgroundClass: "from-red-50 to-rose-50",
    borderClass: "border-red-200",
  },
};

export function formatConfidence(value: number) {
  return `${Math.round(value)}%`;
}

export function getConfidenceTier(value: number): ConfidenceTier {
  if (value >= 90) {
    return CONFIDENCE_TIERS.excellent;
  }

  if (value >= 70) {
    return CONFIDENCE_TIERS.high;
  }

  if (value >= 50) {
    return CONFIDENCE_TIERS.medium;
  }

  return CONFIDENCE_TIERS.low;
}

/**
 * Back-compat helper for call sites (e.g. IssueCard's Badge) that only
 * need the color name, not the full tier object.
 */
export function confidenceColor(value: number): BadgeColorName {
  return getConfidenceTier(value).badgeColor;
}
