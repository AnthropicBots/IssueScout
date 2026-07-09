import {
  CheckCircle2,
  CircleDashed,
} from "lucide-react";

interface IssueDistributionProps {
  assigned: number;
  unassigned: number;
}

export default function IssueDistribution({
  assigned,
  unassigned,
}: IssueDistributionProps) {
  const total = assigned + unassigned;

  const assignedWidth =
    total === 0
      ? 0
      : (assigned / total) * 100;

  const unassignedWidth =
    100 - assignedWidth;

  return (
    <div className="rounded-[1.75rem] border border-slate-200 bg-white p-6 shadow-sm transition-all duration-300 hover:shadow-lg">
      {/* Header */}

      <div className="mb-6">
        <h3 className="text-xl font-bold text-slate-900">
          Issue Distribution
        </h3>

        <p className="mt-2 text-sm text-slate-500">
          Assigned versus contributor-ready issues.
        </p>
      </div>

      {/* Progress Bar */}

      <div className="overflow-hidden rounded-full bg-slate-200">
        <div className="flex h-5">
          <div
            className="bg-gradient-to-r from-emerald-500 to-green-600 transition-all duration-700"
            style={{
              width: `${assignedWidth}%`,
            }}
          />

          <div
            className="bg-gradient-to-r from-blue-500 to-cyan-500 transition-all duration-700"
            style={{
              width: `${unassignedWidth}%`,
            }}
          />
        </div>
      </div>

      {/* Statistics */}

      <div className="mt-8 grid gap-4 sm:grid-cols-2">
        <div className="rounded-2xl border border-green-200 bg-green-50 p-5">
          <div className="flex items-center gap-3">
            <div className="rounded-xl bg-green-100 p-3">
              <CheckCircle2
                size={22}
                className="text-green-600"
              />
            </div>

            <div>
              <p className="text-sm font-medium text-slate-500">
                Assigned
              </p>

              <h4 className="text-3xl font-black text-slate-900">
                {assigned}
              </h4>
            </div>
          </div>
        </div>

        <div className="rounded-2xl border border-blue-200 bg-blue-50 p-5">
          <div className="flex items-center gap-3">
            <div className="rounded-xl bg-blue-100 p-3">
              <CircleDashed
                size={22}
                className="text-blue-600"
              />
            </div>

            <div>
              <p className="text-sm font-medium text-slate-500">
                Available
              </p>

              <h4 className="text-3xl font-black text-slate-900">
                {unassigned}
              </h4>
            </div>
          </div>
        </div>
      </div>

      {/* Footer */}

      <div className="mt-8 flex items-center justify-between border-t border-slate-100 pt-5 text-sm text-slate-500">
        <span>Total Issues</span>

        <span className="font-bold text-slate-900">
          {total}
        </span>
      </div>
    </div>
  );
}
