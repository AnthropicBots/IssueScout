import NoResultState from "../status/NoResultState";

export default function EmptyState() {
  return (
    <NoResultState
      title="No Matching Issues Found"
      description="No issues matched your current search, filters, or sorting criteria. Try clearing the search, changing the selected filters, or scan another GitHub repository to discover more contribution opportunities."
    />
  );
}
