export function recommendation(
  confidence: number,
) {
  if (confidence >= 80) {
    return "Highly recommended for contributors.";
  }

  if (confidence >= 60) {
    return "Worth reviewing before contributing.";
  }

  return "Requires manual verification.";
}

export function repositoryHealth(
  confidence: number,
) {
  if (confidence >= 80) {
    return "Excellent";
  }

  if (confidence >= 60) {
    return "Good";
  }

  return "Needs Review";
}
