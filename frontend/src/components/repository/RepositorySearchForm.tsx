import { useEffect, useState } from "react";
import {
  Search,
  Sparkles,
  ArrowRight,
  GitBranch,
} from "lucide-react";

import { useRepositoryScan } from "../../hooks/useRepositoryScan";

import Button from "../ui/Button";
import Card from "../ui/Card";
import Input from "../ui/Input";
import LoadingSpinner from "../ui/LoadingSpinner";

import ErrorState from "../status/ErrorState";
import LoadingState from "../status/LoadingState";

import RepositoryResults from "./RepositoryResults";

export default function RepositorySearchForm() {
  const [owner, setOwner] = useState(() => {
    return sessionStorage.getItem("issuescout-owner") ?? "";
  });

  const [repository, setRepository] = useState(() => {
    return sessionStorage.getItem("issuescout-repository") ?? "";
  });

  const cachedResult = (() => {
    const data = sessionStorage.getItem(
      "issuescout-last-result",
    );

    return data ? JSON.parse(data) : null;
  })();

  const scan = useRepositoryScan();

  useEffect(() => {
    sessionStorage.setItem(
      "issuescout-owner",
      owner,
    );
  }, [owner]);

  useEffect(() => {
    sessionStorage.setItem(
      "issuescout-repository",
      repository,
    );
  }, [repository]);

  useEffect(() => {
    if (!scan.data) return;

    sessionStorage.setItem(
      "issuescout-last-result",
      JSON.stringify(scan.data),
    );
  }, [scan.data]);

  return (
    <div
      id="repository-scanner"
      className="mt-16 space-y-10"
    >
      <Card className="overflow-hidden rounded-[2rem] border border-slate-800 bg-gradient-to-br from-slate-950 via-slate-900 to-blue-950 text-white shadow-[0_35px_90px_rgba(15,23,42,0.35)]">
        <div className="space-y-10 p-8 lg:p-12">
          {/* Header */}

          <div className="space-y-5 text-center">
            <div className="mx-auto flex h-20 w-20 items-center justify-center rounded-3xl border border-white/10 bg-white/10 shadow-lg backdrop-blur-xl">
              <GitBranch
                size={40}
                className="text-cyan-300"
              />
            </div>

            <div className="space-y-3">
              <h2 className="text-4xl font-extrabold tracking-tight lg:text-5xl">
                Analyze Any GitHub Repository
              </h2>

              <p className="mx-auto max-w-3xl text-lg leading-8 text-slate-300">
                Enter a public GitHub repository to analyze
                open issues, discover contributor-friendly
                tasks, predict pull request relationships,
                evaluate confidence scores, and identify the
                best opportunities for meaningful
                open-source contributions.
              </p>
            </div>
          </div>

          {/* Search Form */}

          <form
            className="grid gap-5 rounded-2xl border border-white/10 bg-white/5 p-5 backdrop-blur-xl lg:grid-cols-[1fr_1fr_auto]"
            onSubmit={(e) => {
              e.preventDefault();

              if (!owner.trim() || !repository.trim()) {
                return;
              }

              scan.mutate({
                owner: owner.trim(),
                repository: repository.trim(),
              });
            }}
          >
            <Input
              placeholder="Repository Owner (e.g. angular)"
              value={owner}
              onChange={(e) =>
                setOwner(
                  e.target.value.replace(/\s/g, "")
                )
              }
            />

            <Input
              placeholder="Repository Name (e.g. angular)"
              value={repository}
              onChange={(e) =>
                setRepository(
                  e.target.value.replace(/\s/g, "")
                )
              }
            />

            <Button
              type="submit"
              className="flex min-h-[52px] items-center justify-center gap-2 whitespace-nowrap"
              disabled={
                scan.isPending ||
                !owner.trim() ||
                !repository.trim()
              }
            >
              {scan.isPending ? (
                <>
                  <LoadingSpinner />
                  Scanning Repository...
                </>
              ) : (
                <>
                  <Search size={18} />
                  Scan Repository
                </>
              )}
            </Button>
          </form>

          <p className="text-center text-sm text-slate-300">
            Press{" "}
            <kbd className="rounded border border-white/20 bg-white/10 px-2 py-1 text-xs">
              Enter
            </kbd>{" "}
            to start scanning.
          </p>

          {/* Popular Repositories */}

          <div>
            <p className="mb-4 text-sm font-semibold uppercase tracking-[0.2em] text-slate-300">
              Popular Repositories
            </p>

            <div className="flex flex-wrap gap-3">
              {[
                "microsoft/vscode",
                "angular/angular",
                "facebook/react",
                "pallets/flask",
                "fastapi/fastapi",
              ].map((repo) => (
                <button
                  key={repo}
                  type="button"
                  onClick={() => {
                    const [o, r] = repo.split("/");

                    setOwner(o);
                    setRepository(r);
                  }}
                  className="rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm font-medium transition-all duration-200 hover:-translate-y-0.5 hover:border-cyan-400/30 hover:bg-white/10"
                >
                  {repo}
                </button>
              ))}
            </div>
          </div>

          {/* Features */}

          <div className="grid gap-5 md:grid-cols-3">
            <div className="rounded-2xl border border-white/10 bg-white/5 p-6 backdrop-blur transition-all duration-200 hover:-translate-y-1 hover:border-cyan-400/20 hover:bg-white/10">
              <Sparkles
                className="mb-4 text-cyan-300"
                size={26}
              />

              <h3 className="text-lg font-semibold">
                AI Predictions
              </h3>

              <p className="mt-3 text-sm leading-7 text-slate-300">
                Predict linked pull requests with intelligent
                confidence scoring and repository analysis.
              </p>
            </div>

            <div className="rounded-2xl border border-white/10 bg-white/5 p-6 backdrop-blur transition-all duration-200 hover:-translate-y-1 hover:border-cyan-400/20 hover:bg-white/10">
              <GitBranch
                className="mb-4 text-blue-300"
                size={26}
              />

              <h3 className="text-lg font-semibold">
                GitHub Analysis
              </h3>

              <p className="mt-3 text-sm leading-7 text-slate-300">
                Analyze repositories in real time using the
                GitHub API and advanced repository
                intelligence.
              </p>
            </div>

            <div className="rounded-2xl border border-white/10 bg-white/5 p-6 backdrop-blur transition-all duration-200 hover:-translate-y-1 hover:border-cyan-400/20 hover:bg-white/10">
              <ArrowRight
                className="mb-4 text-emerald-300"
                size={26}
              />

              <h3 className="text-lg font-semibold">
                Contribution Ready
              </h3>

              <p className="mt-3 text-sm leading-7 text-slate-300">
                Discover high-quality issues that are ready
                for contributors in just a few seconds.
              </p>
            </div>
          </div>
        </div>
      </Card>

      {scan.isPending && (
        <LoadingState
          title="Scanning Repository..."
          description="Fetching issues, analyzing pull requests, calculating confidence scores, and preparing contributor insights."
        />
      )}

      {scan.error && (
        <ErrorState
          title="Repository Scan Failed"
          message={
            scan.error instanceof Error
              ? scan.error.message
              : "Unable to scan the selected repository."
          }
        />
      )}

      {(scan.data || cachedResult) && (
        <RepositoryResults
          result={scan.data ?? cachedResult}
          owner={owner}
          repo={repository}
        />
      )}
    </div>
  );
}
