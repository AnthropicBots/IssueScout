import Badge from "../ui/Badge";

interface IssueMetadataProps {
  confidence: number;
  assigned: boolean;
}

export default function IssueMetadata({
  confidence,
  assigned,
}: IssueMetadataProps) {
  const confidenceColor =
    confidence >= 80
      ? "green"
      : confidence >= 50
      ? "yellow"
      : "red";

  return (
    <div className="flex flex-wrap gap-3">

      <Badge color={confidenceColor}>
        {confidence}% Confidence
      </Badge>

      <Badge
        color={assigned ? "green" : "red"}
      >
        {assigned
          ? "Assigned"
          : "Unassigned"}
      </Badge>

    </div>
  );
}
