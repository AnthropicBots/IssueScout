import { useState } from "react";
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
  const [owner, setOwner] = useState("");
  const [repository, setRepository] = useState("");

  const scan = useRepositoryScan();

  return (
    <div className="mt-12 space-y-8">

      <Card className="overflow-hidden border-0 bg-gradient-to-br from-slate-900 via-slate-800 to-blue-900 text-white shadow-2xl">

        <div className="space-y-8 p-8 lg:p-12">

          {/* Header */}

          <div className="space-y-4 text-center">

            <div className="mx-auto flex h-20 w-20 items-center justify-center rounded-3xl bg-white/10 backdrop-blur">
              <GitBranch size={42} />
            </div>

            <h2 className="text-4xl font-bold">
              Scan Any GitHub Repository
            </h2>

            <p className="mx-auto max-w-3xl text-lg text-slate-300">
              Discover contribution opportunities using
              IssueScout's intelligent prediction engine.
              Analyze issues, confidence scores,
              assignments, and linked pull requests in
              seconds.
            </p>

          </div>

          {/* Search */}

          <form
            className="grid gap-4 lg:grid-cols-[1fr_1fr_auto]"
            onSubmit={(e) => {
              e.preventDefault();

              if (!owner.trim() || !repository.trim()) return;

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
                setOwner(e.target.value.replace(/\s/g, ""))
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
              className="flex items-center justify-center gap-2"
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

          {/* Quick Examples */}

          <div>

            <p className="mb-3 text-sm font-semibold uppercase tracking-wider text-slate-300">
              Popular repositories
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
                  onClick={() => {
                    const [o, r] =
                      repo.split("/");

                    setOwner(o);
                    setRepository(r);
                  }}
                  className="rounded-full border border-white/20 bg-white/10 px-4 py-2 text-sm transition hover:bg-white/20"
                >
                  {repo}
                </button>
              ))}

            </div>

          </div>

          {/* Features */}

          <div className="grid gap-4 md:grid-cols-3">

            <div className="rounded-xl bg-white/10 p-5 backdrop-blur">

              <Sparkles className="mb-3" />

              <h3 className="font-semibold">
                AI Predictions
              </h3>

              <p className="mt-2 text-sm text-slate-300">
                Predict linked pull requests with
                confidence scoring.
              </p>

            </div>

            <div className="rounded-xl bg-white/10 p-5 backdrop-blur">

              <GitBranch className="mb-3" />

              <h3 className="font-semibold">
                GitHub Analysis
              </h3>

              <p className="mt-2 text-sm text-slate-300">
                Analyze repositories in real time
                using the GitHub API.
              </p>

            </div>

            <div className="rounded-xl bg-white/10 p-5 backdrop-blur">

              <ArrowRight className="mb-3" />

              <h3 className="font-semibold">
                Contribution Ready
              </h3>

              <p className="mt-2 text-sm text-slate-300">
                Quickly discover issues ready for
                contributors.
              </p>

            </div>

          </div>

        </div>

      </Card>

      {scan.isPending && (
        <LoadingState
          title="Scanning Repository..."
          description="Fetching issues, analyzing pull requests, and calculating prediction confidence."
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

      {scan.data && (
        <RepositoryResults
          result={scan.data}
          owner={owner}
          repo={repository}
        />
      )}

    </div>
  );
}
