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
    total === 0 ? 0 : (assigned / total) * 100;

  const unassignedWidth = 100 - assignedWidth;

  return (
    <div className="rounded-xl border border-slate-200 bg-white p-6">

      <h3 className="font-semibold">
        Issue Distribution
      </h3>

      <div className="mt-6 flex h-5 overflow-hidden rounded-full">

        <div
          className="bg-green-500"
          style={{
            width: `${assignedWidth}%`,
          }}
        />

        <div
          className="bg-blue-500"
          style={{
            width: `${unassignedWidth}%`,
          }}
        />

      </div>

      <div className="mt-4 flex justify-between text-sm">

        <span>
          Assigned ({assigned})
        </span>

        <span>
          Unassigned ({unassigned})
        </span>

      </div>

    </div>
  );
}
