import {
  Activity,
  CheckCircle,
  FolderGit2,
  Target,
  TrendingUp,
  BarChart3,
} from "lucide-react";

import ConfidenceGauge from "../charts/ConfidenceGauge";
import IssueDistribution from "../charts/IssueDistribution";
import RepositoryHealthChart from "../charts/RepositoryHealthChart";
import {
  assignedIssues,
} from "../../utils/helpers/repository";

import {
  repositoryHealth,
} from "../../utils/helpers/prediction";
interface RepositoryOverviewProps {
  repository: string;
  totalIssues: number;
  availableIssues: number;
  averageConfidence: number;
}

export default function RepositoryOverview({
  repository,
  totalIssues,
  availableIssues,
  averageConfidence,
}: RepositoryOverviewProps) {
  const totalAssigned = assignedIssues(
    totalIssues,
    availableIssues,
  );

  const health =
    repositoryHealth(
      averageConfidence,
    );
  return (
    <div className="space-y-6">

      <div>
        <h2 className="text-3xl font-bold text-slate-900">
          Repository Dashboard
        </h2>

        <p className="mt-2 text-slate-500">
          Analysis summary for{" "}
          <span className="font-semibold">
            {repository}
          </span>
        </p>
      </div>

      <StatisticsGrid>

        <StatisticsCard
          title="Repository"
          value={repository}
          icon={<FolderGit2 size={22} />}
          color="bg-indigo-100 text-indigo-600"
        />

        <StatisticsCard
          title="Total Issues"
          value={totalIssues}
          icon={<Activity size={22} />}
          color="bg-blue-100 text-blue-600"
        />

        <StatisticsCard
          title="Available"
          value={availableIssues}
          icon={<CheckCircle size={22} />}
          color="bg-green-100 text-green-600"
        />

        <StatisticsCard
          title="Assigned"
          value={totalAssigned}
          icon={<BarChart3 size={22} />}
          color="bg-orange-100 text-orange-600"
        />

        <StatisticsCard
          title="Average Confidence"
          value={`${averageConfidence}%`}
          icon={<Target size={22} />}
          color="bg-cyan-100 text-cyan-600"
        />

        <StatisticsCard
          title="Repository Health"
          value={health}
          icon={<TrendingUp size={22} />}
          color="bg-emerald-100 text-emerald-600"
        />

      </StatisticsGrid>

      <div className="grid gap-6 lg:grid-cols-3">

        <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
          <ConfidenceGauge
            value={averageConfidence}
          />
        </div>

        <IssueDistribution
          assigned={totalAssigned}
          unassigned={availableIssues}
        />

        <RepositoryHealthChart
          score={averageConfidence}
        />

      </div>

    </div>
  );
}
