import {
  Activity,
  GitBranch,
  SearchCode,
} from "lucide-react";

export default function Header() {
  return (
    <header className="sticky top-0 z-50 border-b border-slate-200 bg-white/90 backdrop-blur">
      <div className="mx-auto flex h-20 max-w-7xl items-center justify-between px-6">

        {/* Logo */}

        <div className="flex items-center gap-4">

          <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-gradient-to-br from-blue-600 to-indigo-600 text-white shadow-lg">

            <SearchCode size={26} />

          </div>

          <div>

            <h1 className="text-xl font-bold tracking-tight text-slate-900">
              IssueScout
            </h1>

            <p className="text-sm text-slate-500">
              Intelligent GitHub Contribution Assistant
            </p>

          </div>

        </div>

        {/* Right Side */}

        <div className="flex items-center gap-4">

          {/* API Status */}

          <div className="hidden items-center gap-2 rounded-full bg-green-100 px-3 py-2 md:flex">

            <Activity
              size={14}
              className="text-green-600"
            />

            <span className="text-sm font-medium text-green-700">
              API Online
            </span>

          </div>

          {/* Version */}

          <div className="hidden rounded-full bg-slate-100 px-3 py-2 text-sm font-medium text-slate-600 lg:block">
            v1.0.0
          </div>

          {/* GitHub */}

          <button
            type="button"
            className="flex h-11 w-11 items-center justify-center rounded-xl border border-slate-200 transition hover:bg-slate-100"
            title="GitHub Repository"
          >
            <GitBranch
              size={20}
              className="text-slate-600"
            />
          </button>

        </div>

      </div>
    </header>
  );
}
