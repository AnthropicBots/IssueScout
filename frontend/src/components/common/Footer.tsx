import {
  Activity,
  Code2,
  Database,
  ExternalLink,
  GitBranch,
  Heart,
} from "lucide-react";

export default function Footer() {
  return (
    <footer className="border-t border-slate-200 bg-slate-50">
      <div className="mx-auto max-w-7xl px-6 py-12">

        <div className="grid gap-10 lg:grid-cols-4">

          {/* Brand */}

          <div className="space-y-4">

            <h2 className="text-2xl font-bold text-slate-900">
              IssueScout
            </h2>

            <p className="leading-7 text-slate-600">
              Intelligent GitHub Issue Discovery and
              Contribution Analysis powered by repository
              insights and smart issue ranking.
            </p>

          </div>

          {/* Features */}

          <div>

            <h3 className="mb-4 font-semibold text-slate-900">
              Features
            </h3>

            <ul className="space-y-3 text-slate-600">
              <li>Repository Analysis</li>
              <li>Issue Prediction</li>
              <li>Contribution Insights</li>
              <li>Pull Request Linking</li>
            </ul>

          </div>

          {/* Technology */}

          <div>

            <h3 className="mb-4 font-semibold text-slate-900">
              Built With
            </h3>

            <div className="space-y-3">

              <div className="flex items-center gap-2 text-slate-600">
                <Code2 size={18} />
                React + TypeScript
              </div>

              <div className="flex items-center gap-2 text-slate-600">
                <Database size={18} />
                FastAPI Backend
              </div>

              <div className="flex items-center gap-2 text-slate-600">
                <GitBranch size={18} />
                GitHub REST API
              </div>

            </div>

          </div>

          {/* Status */}

          <div>

            <h3 className="mb-4 font-semibold text-slate-900">
              Project
            </h3>

            <div className="space-y-4">

              <div className="inline-flex items-center gap-2 rounded-full bg-green-100 px-4 py-2">

                <Activity
                  size={16}
                  className="text-green-600"
                />

                <span className="font-medium text-green-700">
                  Backend Online
                </span>

              </div>

              <a
                href="https://github.com/YOUR_USERNAME/IssueScout"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-medium text-slate-700 transition hover:bg-slate-100"
              >
                <GitBranch size={16} />
                GitHub Repository
                <ExternalLink size={14} />
              </a>

            </div>

          </div>

        </div>

        {/* Bottom */}

        <div className="mt-10 flex flex-col items-center justify-between gap-4 border-t border-slate-200 pt-6 text-sm text-slate-500 md:flex-row">

          <p>
            © {new Date().getFullYear()}{" "}
            <span className="font-semibold text-slate-700">
              IssueScout
            </span>
            {" "}• Open Source Project
          </p>

          <div className="flex items-center gap-2">

            <span>Made with</span>

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
