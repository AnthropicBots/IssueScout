import {
  Activity,
  Code2,
  Database,
  GitBranch,
  Heart,
} from "lucide-react";

export default function Footer() {
  return (
    <footer className="mt-20 border-t border-slate-200 bg-slate-50">
      <div className="mx-auto max-w-7xl px-6 py-12">

        <div className="grid gap-10 lg:grid-cols-4">

          {/* Brand */}

          <div className="space-y-4">

            <h2 className="text-2xl font-bold text-slate-900">
              IssueScout
            </h2>

            <p className="leading-7 text-slate-600">
              Intelligent GitHub Issue Discovery &
              Contribution Analysis platform powered
              by AI-assisted repository insights.
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
              System Status
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

              <div className="rounded-xl border border-slate-200 bg-white p-4">

                <p className="text-sm text-slate-500">
                  Version
                </p>

                <p className="mt-1 font-semibold text-slate-900">
                  v1.0.0
                </p>

              </div>

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
            . All rights reserved.
          </p>

          <div className="flex items-center gap-2">

            <span>Made with</span>

            <Heart
              size={16}
              className="fill-red-500 text-red-500"
            />

            <span>for the Open Source Community.</span>

          </div>

        </div>

      </div>
    </footer>
  );
}
