import {
  ArrowLeft,
  Compass,
  Home,
  SearchCode,
} from "lucide-react";

import { Link } from "react-router-dom";

export default function NotFoundPage() {
  return (
    <main className="flex min-h-[75vh] items-center justify-center px-6 py-16">
      <div className="w-full max-w-4xl overflow-hidden rounded-[2rem] border border-slate-200 bg-white shadow-[0_30px_70px_rgba(15,23,42,0.12)]">
        {/* Hero */}

        <div className="relative overflow-hidden bg-gradient-to-br from-slate-950 via-slate-900 to-blue-950 px-10 py-16 text-center text-white">
          <div className="absolute -left-20 -top-20 h-64 w-64 rounded-full bg-cyan-400/20 blur-3xl" />

          <div className="absolute -bottom-20 -right-20 h-72 w-72 rounded-full bg-blue-500/20 blur-3xl" />

          <div className="relative">
            <div className="mx-auto flex h-24 w-24 items-center justify-center rounded-3xl bg-white/10 backdrop-blur">
              <SearchCode
                size={44}
                className="text-cyan-300"
              />
            </div>

            <h1 className="mt-8 text-8xl font-black tracking-tight text-cyan-300">
              404
            </h1>

            <h2 className="mt-4 text-4xl font-black">
              Page Not Found
            </h2>

            <p className="mx-auto mt-6 max-w-2xl text-lg leading-8 text-slate-300">
              The page you're looking for doesn't exist,
              may have been moved, or the repository
              analysis is no longer available.
            </p>
          </div>
        </div>

        {/* Content */}

        <div className="space-y-8 p-10">
          <div className="grid gap-6 md:grid-cols-3">
            <div className="rounded-2xl border border-slate-200 bg-slate-50 p-6">
              <div className="mb-4 inline-flex rounded-2xl bg-blue-100 p-3">
                <Home
                  size={22}
                  className="text-blue-600"
                />
              </div>

              <h3 className="text-lg font-bold text-slate-900">
                Go Home
              </h3>

              <p className="mt-3 text-sm leading-6 text-slate-600">
                Return to the homepage and scan another
                GitHub repository.
              </p>
            </div>

            <div className="rounded-2xl border border-slate-200 bg-slate-50 p-6">
              <div className="mb-4 inline-flex rounded-2xl bg-green-100 p-3">
                <SearchCode
                  size={22}
                  className="text-green-600"
                />
              </div>

              <h3 className="text-lg font-bold text-slate-900">
                Scan Again
              </h3>

              <p className="mt-3 text-sm leading-6 text-slate-600">
                Start a new repository analysis using the
                IssueScout AI engine.
              </p>
            </div>

            <div className="rounded-2xl border border-slate-200 bg-slate-50 p-6">
              <div className="mb-4 inline-flex rounded-2xl bg-purple-100 p-3">
                <Compass
                  size={22}
                  className="text-purple-600"
                />
              </div>

              <h3 className="text-lg font-bold text-slate-900">
                Continue Exploring
              </h3>

              <p className="mt-3 text-sm leading-6 text-slate-600">
                Discover more repositories and contribution
                opportunities.
              </p>
            </div>
          </div>

          {/* Action */}

          <div className="flex justify-center border-t border-slate-200 pt-8">
            <Link
              to="/"
              className="inline-flex items-center gap-3 rounded-2xl bg-gradient-to-r from-blue-600 to-cyan-500 px-8 py-4 font-semibold text-white shadow-lg transition-all duration-300 hover:-translate-y-1 hover:shadow-2xl"
            >
              <ArrowLeft size={20} />

              Return to Homepage
            </Link>
          </div>
        </div>
      </div>
    </main>
  );
}
