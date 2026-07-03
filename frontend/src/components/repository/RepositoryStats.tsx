import Card from "../ui/Card";

type Props = {
  repository: string;
  totalIssues: number;
  availableIssues: number;
};

export default function RepositoryStats({
  repository,
  totalIssues,
  availableIssues,
}: Props) {
  return (
    <Card>
      <div className="flex flex-col gap-6 md:flex-row md:items-center md:justify-between">
        <div>
          <h2 className="text-3xl font-bold">
            {repository}
          </h2>

          <p className="mt-2 text-slate-500">
            Repository Scan Summary
          </p>
        </div>

        <div className="flex gap-10">
          <div>
            <p className="text-sm text-slate-500">
              Total Issues
            </p>

            <p className="text-2xl font-bold">
              {totalIssues}
            </p>
          </div>

          <div>
            <p className="text-sm text-slate-500">
              Available Issues
            </p>

            <p className="text-2xl font-bold text-blue-600">
              {availableIssues}
            </p>
          </div>
        </div>
      </div>
    </Card>
  );
}
