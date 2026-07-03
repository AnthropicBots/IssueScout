export function assignedIssues(
  total: number,
  available: number,
) {
  return Math.max(
    total - available,
    0,
  );
}

export function averageConfidence(
  values: number[],
) {
  if (values.length === 0) {
    return 0;
  }

  return Math.round(
    values.reduce(
      (sum, value) => sum + value,
      0,
    ) / values.length,
  );
}
