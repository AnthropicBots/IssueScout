import {
  Activity,
  ArrowUpRight,
  GitBranch,
  SearchCode,
  Sparkles,
} from "lucide-react";
import { Link } from "react-router-dom";

export default function Header() {
  return (
    <header className="sticky top-0 z-50 border-b border-slate-200/80 bg-white/80 backdrop-blur-xl">
      <div className="mx-auto flex h-20 max-w-7xl items-center justify-between px-6">
        {/* Logo */}

        <Link
          to="/"
          className="group flex items-center gap-4"
          aria-label="IssueScout Home"
        >
          <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-gradient-to-br from-blue-600 via-cyan-500 to-indigo-600 text-white shadow-lg transition-transform duration-300 group-hover:scale-110">
            <SearchCode size={24} />
          </div>

          <div>
            <h1 className="text-2xl font-black tracking-tight text-slate-900">
              IssueScout
            </h1>

            <p className="text-sm text-slate-500">
              AI-Powered GitHub Contribution Assistant
            </p>
          </div>
        </Link>

        {/* Right Side */}

        <div className="flex items-center gap-3">
          {/* Status */}

          <div className="hidden items-center gap-2 rounded-full border border-green-200 bg-green-50 px-4 py-2 md:flex">
            <Activity
              size={14}
              className="text-green-600"
            />

            <span className="text-sm font-semibold text-green-700">
              API Online
            </span>
          </div>

          {/* Version */}

          <div className="hidden items-center gap-2 rounded-full border border-blue-200 bg-blue-50 px-4 py-2 lg:flex">
            <Sparkles
              size={14}
              className="text-blue-600"
            />

            <span className="text-sm font-semibold text-blue-700">
              v1.0.0
            </span>
          </div>

          {/* GitHub */}

          <a
            href="https://github.com/AnthropicBots/IssueScout"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="View IssueScout on GitHub"
            className="group flex items-center gap-2 rounded-xl border border-slate-200 bg-white px-4 py-2.5 text-sm font-semibold text-slate-700 shadow-sm transition-all duration-200 hover:-translate-y-0.5 hover:border-blue-200 hover:bg-slate-50 hover:shadow-md"
          >
            <GitBranch
              size={18}
              className="transition-colors group-hover:text-blue-600"
            />

            <span className="hidden sm:inline">
              GitHub
            </span>

            <ArrowUpRight
              size={16}
              className="transition-transform duration-200 group-hover:translate-x-0.5 group-hover:-translate-y-0.5"
            />
          </a>
        </div>
      </div>
    </header>
  );
}
