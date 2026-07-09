import {
  CheckCircle2,
  ShieldCheck,
  UserCheck,
  UserX,
} from "lucide-react";

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
    confidence >= 90
      ? "green"
      : confidence >= 70
      ? "blue"
      : confidence >= 50
      ? "yellow"
      : "red";

  const confidenceLabel =
    confidence >= 90
      ? "Excellent"
      : confidence >= 70
      ? "High"
      : confidence >= 50
      ? "Medium"
      : "Low";

  return (
    <div className="rounded-[1.75rem] border border-slate-200 bg-white p-6 shadow-sm">
      <div className="mb-5 flex items-center gap-2">
        <ShieldCheck
          size={20}
          className="text-blue-600"
        />

        <h3 className="text-lg font-bold text-slate-900">
          Issue Metadata
        </h3>
      </div>

      <div className="flex flex-wrap items-center gap-4">
        <Badge color={confidenceColor}>
          {confidence}% Confidence
        </Badge>

        <Badge color={confidenceColor}>
          {confidenceLabel}
        </Badge>

        <Badge
          color={assigned ? "green" : "red"}
        >
          {assigned ? (
            <span className="inline-flex items-center gap-1">
              <UserCheck size={14} />
              Assigned
            </span>
          ) : (
            <span className="inline-flex items-center gap-1">
              <UserX size={14} />
              Unassigned
            </span>
          )}
        </Badge>

        <div className="ml-auto hidden items-center gap-2 rounded-full bg-emerald-50 px-4 py-2 text-sm font-medium text-emerald-700 lg:flex">
          <CheckCircle2 size={16} />
          Analysis Complete
        </div>
      </div>
    </div>
  );
}
