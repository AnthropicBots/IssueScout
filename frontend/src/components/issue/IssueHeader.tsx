import {
  ArrowLeft,
  GitBranch,
} from "lucide-react";
import { Link } from "react-router-dom";

interface IssueHeaderProps {
  issueNumber: number;
  title: string;
}

export default function IssueHeader({
  issueNumber,
  title,
}: IssueHeaderProps) {
  return (
    <section className="mb-10">
      <Link
        to="/"
        className="group mb-8 inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white px-5 py-3 text-sm font-semibold text-slate-700 shadow-sm transition-all duration-200 hover:-translate-x-1 hover:border-blue-200 hover:text-blue-600 hover:shadow-md"
      >
        <ArrowLeft
          size={18}
          className="transition-transform duration-200 group-hover:-translate-x-1"
        />

        Back to Repository
      </Link>

      <div className="overflow-hidden rounded-[2rem] border border-slate-200 bg-gradient-to-br from-slate-950 via-slate-900 to-blue-950 text-white shadow-[0_30px_70px_rgba(15,23,42,0.25)]">
        <div className="flex flex-col gap-8 p-8 lg:flex-row lg:items-center lg:justify-between lg:p-10">
          <div className="min-w-0 flex-1">
            <div className="mb-5 inline-flex items-center gap-2 rounded-full border border-cyan-400/30 bg-white/10 px-4 py-2 text-sm font-semibold text-cyan-200 backdrop-blur">
              <GitBranch size={16} />
              GitHub Issue Analysis
            </div>

            <h1 className="text-4xl font-black tracking-tight lg:text-5xl">
              Issue #{issueNumber}
            </h1>

            <p className="mt-5 max-w-3xl text-lg leading-8 text-slate-300">
              {title}
            </p>
          </div>

          <div className="rounded-3xl border border-white/10 bg-white/10 px-8 py-6 text-center backdrop-blur">
            <p className="text-sm uppercase tracking-[0.2em] text-slate-300">
              Issue ID
            </p>

            <h2 className="mt-2 text-5xl font-black text-cyan-300">
              #{issueNumber}
            </h2>
          </div>
        </div>
      </div>
    </section>
  );
}
