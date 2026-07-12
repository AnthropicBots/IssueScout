import {
  CheckCircle2,
  CircleDashed,
  PieChart,
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

  const assignedPercentage =
    total === 0
      ? 0
      : Math.round((assigned / total) * 100);

  const availablePercentage =
    100 - assignedPercentage;

  return (
    <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">

      {/* Header */}

      <div className="flex items-center gap-3">

        <div className="rounded-2xl bg-blue-100 p-3">

          <PieChart
            size={20}
            className="text-blue-600"
          />

        </div>

        <div>

          <h3 className="font-bold text-slate-900">
            Issue Distribution
          </h3>

          <p className="text-sm text-slate-500">
            Assignment overview
          </p>

        </div>

      </div>

      {/* Progress */}

      <div className="mt-8">

        <div className="mb-3 flex justify-between text-sm text-slate-500">

          <span>Assigned</span>

          <span>Available</span>

        </div>

        <div className="flex h-3 overflow-hidden rounded-full bg-slate-200">

          <div
            className="bg-gradient-to-r from-emerald-500 to-green-500 transition-all duration-700"
            style={{
              width: `${assignedPercentage}%`,
            }}
          />

          <div
            className="bg-gradient-to-r from-blue-500 to-cyan-500 transition-all duration-700"
            style={{
              width: `${availablePercentage}%`,
            }}
          />

        </div>

      </div>

      {/* Statistics */}

      <div className="mt-8 space-y-4">

        <div className="flex items-center justify-between rounded-2xl border border-slate-200 p-4">

          <div className="flex items-center gap-3">

            <div className="rounded-xl bg-green-100 p-2">

              <CheckCircle2
                size={18}
                className="text-green-600"
              />

            </div>

            <div>

              <div className="font-semibold text-slate-900">
                Assigned
              </div>

              <div className="text-sm text-slate-500">
                Currently owned
              </div>

            </div>

          </div>

          <div className="text-right">

            <div className="text-2xl font-black text-slate-900">
              {assigned}
            </div>

            <div className="text-xs text-slate-500">
              {assignedPercentage}%
            </div>

          </div>

        </div>

        <div className="flex items-center justify-between rounded-2xl border border-slate-200 p-4">

          <div className="flex items-center gap-3">

            <div className="rounded-xl bg-blue-100 p-2">

              <CircleDashed
                size={18}
                className="text-blue-600"
              />

            </div>

            <div>

              <div className="font-semibold text-slate-900">
                Available
              </div>

              <div className="text-sm text-slate-500">
                Ready to contribute
              </div>

            </div>

          </div>

          <div className="text-right">

            <div className="text-2xl font-black text-slate-900">
              {unassigned}
            </div>

            <div className="text-xs text-slate-500">
              {availablePercentage}%
            </div>

          </div>

        </div>

      </div>

      {/* Footer */}

      <div className="mt-8 rounded-2xl bg-slate-50 p-4">

        <div className="flex items-center justify-between">

          <span className="text-slate-600">
            Total Issues
          </span>

          <span className="text-xl font-bold text-slate-900">
            {total}
          </span>

        </div>

      </div>

    </div>
  );
}
