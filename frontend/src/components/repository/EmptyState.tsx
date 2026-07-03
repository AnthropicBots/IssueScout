import NoResultState from "../status/NoResultState";

export default function EmptyState() {
  return (
    <NoResultState
      title="No Issues Found"
      description="IssueScout couldn't find any issues matching the current repository or filters. Try scanning another repository or adjusting your search criteria."
    />
  );
}
