export function assignedIssues(
  total: number,
  available: number,
) {
  return Math.max(
    total - available,
    0,
  );
}
