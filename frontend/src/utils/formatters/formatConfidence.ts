export function formatConfidence(value: number) {
  return `${Math.round(value)}%`;
}

export function confidenceColor(
  value: number,
): "green" | "yellow" | "red" {
  if (value >= 80) {
    return "green";
  }

  if (value >= 50) {
    return "yellow";
  }

  return "red";
}

export function confidenceLabel(
  value: number,
) {
  if (value >= 80) {
    return "High";
  }

  if (value >= 50) {
    return "Medium";
  }

  return "Low";
}
