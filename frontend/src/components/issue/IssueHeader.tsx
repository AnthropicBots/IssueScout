import {
  ArrowLeft,
  Calendar,
  ExternalLink,
  FolderGit2,
  GitBranch,
  User,
} from "lucide-react";
import { Link } from "react-router-dom";

interface IssueHeaderProps {
  issueNumber: number;
  title: string;
  owner?: string;
  repository?: string;
  author?: string;
  createdAt?: string;
  updatedAt?: string;
}

function formatDate(date?: string) {
  if (!date) return "-";

  return new Date(date).toLocaleDateString(undefined, {
    year: "numeric",
    month: "short",
    day: "numeric",
  });
}

export default function IssueHeader({
  issueNumber,
  title,
  owner,
  repository,
  author,
  createdAt,
  updatedAt,
}: IssueHeaderProps) {
  const issueUrl =
    owner && repository
      ? `https://github.com/${owner}/${repository}/issues/${issueNumber}`
      : undefined;

  return (
    <section className="mb-8">

      {/* Top Actions */}

      <div className="mb-6 flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">

        <Link
          to="/"
          className="inline-flex w-fit items-center gap-2 rounded-2xl border border-slate-200 bg-white px-5 py-3 font-semibold text-slate-700 shadow-sm transition hover:border-blue-200 hover:text-blue-600 hover:shadow-md"
        >
          <ArrowLeft size={18} />
          Back to Repository
        </Link>

        <div className="flex flex-wrap gap-3">

          {issueUrl && (
            <a
              href={issueUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 rounded-2xl border border-slate-200 bg-white px-5 py-3 font-semibold text-slate-800 shadow-sm transition hover:border-blue-200 hover:text-blue-600 hover:shadow-md"
            >
              <ExternalLink size={18} />
              Open on GitHub
            </a>
          )}

        </div>

      </div>

      {/* Hero */}

      <div className="rounded-3xl border border-slate-200 bg-white shadow-sm">

        <div className="grid gap-8 p-8 lg:grid-cols-[1.7fr_1fr]">

          {/* Left */}

          <div>

            <div className="inline-flex items-center gap-2 rounded-full bg-blue-50 px-4 py-2 text-sm font-semibold text-blue-700">
              <GitBranch size={15} />
              GitHub Issue Analysis
            </div>

            <h1 className="mt-5 text-4xl font-black text-slate-900">
              Issue #{issueNumber}
            </h1>

            <p className="mt-4 max-w-3xl text-lg text-slate-600">
              {title}
            </p>

          </div>

          {/* Right */}

          <div className="grid grid-cols-2 gap-5">

            <div>
              <div className="flex items-center gap-2 text-sm font-semibold uppercase tracking-wide text-slate-500">
                <FolderGit2 size={16} />
                Repository
              </div>

              <p className="mt-2 font-bold text-slate-900">
                {owner && repository
                  ? `${owner}/${repository}`
                  : "-"}
              </p>
            </div>

            <div>
              <div className="flex items-center gap-2 text-sm font-semibold uppercase tracking-wide text-slate-500">
                <User size={16} />
                Author
              </div>

              <p className="mt-2 font-bold text-slate-900">
                {author ?? "-"}
              </p>
            </div>

            <div>
              <div className="flex items-center gap-2 text-sm font-semibold uppercase tracking-wide text-slate-500">
                <Calendar size={16} />
                Created
              </div>

              <p className="mt-2 font-bold text-slate-900">
                {formatDate(createdAt)}
              </p>
            </div>

            <div>
              <div className="flex items-center gap-2 text-sm font-semibold uppercase tracking-wide text-slate-500">
                <Calendar size={16} />
                Updated
              </div>

              <p className="mt-2 font-bold text-slate-900">
                {formatDate(updatedAt)}
              </p>
            </div>

          </div>

        </div>

      </div>

    </section>
  );
}
