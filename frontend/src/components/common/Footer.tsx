import {
  Activity,
  Code2,
  Database,
  ExternalLink,
  GitBranch,
  Heart,
  Sparkles,
} from "lucide-react";

export default function Footer() {
  return (
    <footer className="mt-24 border-t border-slate-200 bg-gradient-to-b from-slate-50 to-white">
      <div className="mx-auto max-w-7xl px-6 py-16">
        <div className="grid gap-12 lg:grid-cols-4">
          {/* Brand */}

          <div className="space-y-5">
            <div className="inline-flex items-center gap-3">
              <div className="rounded-2xl bg-gradient-to-br from-blue-600 to-cyan-500 p-3 text-white shadow-lg">
                <Sparkles size={22} />
              </div>

              <h2 className="text-3xl font-black tracking-tight text-slate-900">
                IssueScout
              </h2>
            </div>

            <p className="leading-8 text-slate-600">
              Intelligent GitHub issue discovery and repository
              analysis powered by AI-driven confidence scoring,
              contributor insights, and pull request prediction.
            </p>
          </div>

          {/* Features */}

          <div>
            <h3 className="mb-5 text-lg font-bold text-slate-900">
              Features
            </h3>

            <ul className="space-y-3 text-slate-600">
              <li>Repository Analysis</li>
              <li>AI Issue Prediction</li>
              <li>Confidence Scoring</li>
              <li>Contribution Insights</li>
              <li>Pull Request Detection</li>
            </ul>
          </div>

          {/* Technology */}

          <div>
            <h3 className="mb-5 text-lg font-bold text-slate-900">
              Built With
            </h3>

            <div className="space-y-4">
              <div className="flex items-center gap-3 text-slate-600">
                <Code2
                  size={18}
                  className="text-blue-600"
                />
                React + TypeScript
              </div>

              <div className="flex items-center gap-3 text-slate-600">
                <Database
                  size={18}
                  className="text-emerald-600"
                />
                FastAPI Backend
              </div>

              <div className="flex items-center gap-3 text-slate-600">
                <GitBranch
                  size={18}
                  className="text-violet-600"
                />
                GitHub REST API
              </div>
            </div>
          </div>

          {/* Project */}

          <div>
            <h3 className="mb-5 text-lg font-bold text-slate-900">
              Project
            </h3>

            <div className="space-y-5">
              <div className="inline-flex items-center gap-2 rounded-full bg-green-100 px-4 py-2">
                <Activity
                  size={16}
                  className="text-green-600"
                />

                <span className="font-semibold text-green-700">
                  Production Ready
                </span>
              </div>

              <a
                href="https://github.com/AnthropicBots/IssueScout"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 rounded-xl border border-slate-200 bg-white px-5 py-3 text-sm font-semibold text-slate-700 shadow-sm transition-all duration-200 hover:-translate-y-0.5 hover:border-blue-200 hover:bg-slate-50 hover:shadow-md"
              >
                <GitBranch size={16} />

                View on GitHub

                <ExternalLink size={14} />
              </a>
            </div>
          </div>
        </div>

        {/* Bottom */}

        <div className="mt-14 flex flex-col items-center justify-between gap-4 border-t border-slate-200 pt-8 text-sm text-slate-500 md:flex-row">
          <p>
            © {new Date().getFullYear()}{" "}
            <span className="font-semibold text-slate-700">
              IssueScout
            </span>{" "}
            · Open Source Project
          </p>

          <div className="flex items-center gap-2">
            <span>Built with</span>

            <Heart
              size={16}
              className="fill-red-500 text-red-500"
            />

            <span>for the Open Source Community</span>
          </div>
        </div>
      </div>
    </footer>
  );
}
